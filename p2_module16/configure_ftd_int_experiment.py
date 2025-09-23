#configure_ftd_int
"""
This test will configure the FTD interfaces
"""

from pyats import aetest, topology
import math

from lib.connectors.swagger_con import SwaggerConnector


class ConnectFTDREST(aetest.Testcase):
    """
    This test will configure the FTD interfaces
    """
    @aetest.test
    def load_testbed(self, steps):
        """ This method will load the testbed """
        with steps.start("Load testbed"):
            tb = topology.loader.load('ftd_testbed.yaml')
            self.parent.parameters.update(tb=tb)

    @aetest.test
    def connect_via_rest(self, steps):  # pylint: disable=missing-function-docstring,too-many-locals
        tb = self.parent.parameters.get('tb')
        with steps.start("Connect via rest"):
            for device in tb.devices:
                if tb.devices[device].type != 'firewall':
                    continue
                if "swagger" not in tb.devices[device].connections:
                    continue
                connection: SwaggerConnector = tb.devices[device].connect(via='swagger')
                swagger = connection.get_swagger_client()
                if not swagger:
                    self.failed('No swagger connection')
                print(swagger)

        with steps.start("Delete existing DHCP server"):
                 dhcp_servers = swagger.DHCPServerContainer.getDHCPServerContainerList().result()
                 for dhcp_server in dhcp_servers['items']:
                    dhcp_serv_list = dhcp_server['servers']
                    print(dhcp_serv_list)
                    dhcp_server.servers = []
                    response = swagger.DHCPServerContainer.editDHCPServerContainer(
                         objId=dhcp_server.id,
                         body=dhcp_server,
                     ).result()
                    print(response)

        with steps.start('Configure FTD Interfaces'):
            existing_interfaces = swagger.Interface.getPhysicalInterfaceList().result()
            csr_ftd = connection.device.interfaces['csr_ftd']
            ftd_ep2 = connection.device.interfaces['ftd_ep2']
            interface_for_dhcp = None

            print("=== Existing interfaces from FTD ===")
            for interface in existing_interfaces['items']:
                print(f"hardwareName={interface.hardwareName}, "
                      f"name={interface.name}, id={interface.id}")

            for interface in existing_interfaces['items']:
                # match pentru csr_ftd
                if interface.hardwareName.lower() in csr_ftd.name.lower():
                    interface.ipv4.ipAddress.ipAddress = csr_ftd.ipv4.ip.compressed
                    interface.ipv4.ipAddress.netmask = csr_ftd.ipv4.netmask.exploded
                    interface.ipv4.dhcp = False
                    interface.ipv4.ipType = 'STATIC'
                    interface.enable = True
                    interface.name = csr_ftd.alias
                    response = swagger.Interface.editPhysicalInterface(
                        objId=interface.id,
                        body=interface,
                    ).result()
                    print("Configured csr_ftd:", response)

                # match pentru ftd_ep2
                if interface.hardwareName.lower() in ftd_ep2.name.lower():
                    interface.ipv4.ipAddress.ipAddress = ftd_ep2.ipv4.ip.compressed
                    interface.ipv4.ipAddress.netmask = ftd_ep2.ipv4.netmask.exploded
                    interface.ipv4.dhcp = False
                    interface.ipv4.ipType = 'STATIC'
                    interface.enable = True
                    interface.name = ftd_ep2.alias
                    response = swagger.Interface.editPhysicalInterface(
                        objId=interface.id,
                        body=interface,
                    ).result()
                    interface_for_dhcp = interface
                    print("Configured ftd_ep2:", response)

            if not interface_for_dhcp:
                self.failed(
                    f"Nu am găsit interfața pentru DHCP. "
                    f"Testbed: {ftd_ep2.name}, "
                    f"Disponibile: {[i.hardwareName for i in existing_interfaces['items']]}"
                )

        with steps.start("Add DHCP server to interface"):
            dhcp_servers = swagger.DHCPServerContainer.getDHCPServerContainerList().result()
            for dhcp_server in dhcp_servers['items']:
                dhcp_serv_list = dhcp_server['servers']
                print("Existing DHCP servers:", dhcp_serv_list)

                dhcp_server_model = swagger.get_model('DHCPServer')
                interface_ref_model = swagger.get_model('ReferenceModel')

                dhcp_server.servers = [
                    dhcp_server_model(
                        addressPool='192.168.250.50-192.168.250.100',
                        enableDHCP=True,
                        interface=interface_ref_model(
                            id=interface_for_dhcp.id,
                            name=interface_for_dhcp.name,
                            type='physicalinterface'
                        ),
                        type='dhcpserver'
                    )
                ]

                response = swagger.DHCPServerContainer.editDHCPServerContainer(
                    objId=dhcp_server.id,
                    body=dhcp_server,
                ).result()
                print("Configured DHCP server:", response)

        with steps.start("Add routes"):
            pass

        with steps.start("Add allow rule"):
            pass


if __name__ == '__main__':
    aetest.main()
