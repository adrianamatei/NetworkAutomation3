import genie
from genie.libs.conf.base import ipaddress
import ipaddress
from pyats import aetest, topology
from genie.libs.conf.interface.iosxe import Interface
from pyats.topology import Testbed
from genie.libs.conf.static_routing import StaticRouting



class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def load_testbed(self, steps):
        with steps.start("Load testbed"):
            tb = topology.loader.load('new_testbed.yaml')
            self.parent.parameters.update(tb=tb)


class ConfigureGenie(aetest.Testcase):
    @aetest.setup
    def connect(self, steps):
        tb: Testbed = self.parent.parameters.get("tb")
        self.dev = tb.devices.RouterCSR
        self.dev.connect(log_stdout=True)
        #print(dev)
    @aetest.test
    def configure_interfaces(self, steps):
        with steps.start("Configure interface 1"):
            intf = Interface(
                name='GigabitEthernet2'
            )
            intf.device = self.dev
            intf.ipv4 = self.dev.interfaces['GigabitEthernet2'].ipv4
            config = intf.build_config(apply=False)
            self.dev.configure(config.cli_config.data)
            print(config)

        with steps.start("Configure interface 2"):
            intf = Interface(
                name='GigabitEthernet3'
            )
            intf.device = self.dev
            intf.ipv4 = self.dev.interfaces['GigabitEthernet3'].ipv4
            config = intf.build_config(apply=False)
            self.dev.configure(config.cli_config.data)
            print(config)

        # with steps.start("Configure static routing"):
        #     route = StaticRouting()
        #     route.device = self.dev
        #     # route.vrf='default'
        #     # route.address_family='ipv4'
        #     # route.route='192.168.250.0/24'
        #     # route.nexthop='192.168.240.40'
        #
        #     route.device_attr[self.dev].vrf_attr['default'].address_family_attr['ipv4'].route_attr['192.168.250.0/24'].next_hop_attr['192.168.240.40'].set_value(True)
        #     print(route)
        #     print(dir(route))
        #     route.route = ''
        #     config = route.build_config(apply=False)
        #     self.dev.configure(config.cli_config.data)
        with steps.start("Configure static routing"):
            route = StaticRouting()
            route.device = self.dev

            # ia testbed-ul din parametri
            tb: Testbed = self.parent.parameters.get("tb")

            # exemplu: vreau să ajung la LAN-ul din spatele Router (192.168.220.0/24)
            dest_network = ipaddress.IPv4Interface(
                tb.devices.Router.interfaces['GigabitEthernet0/1'].ipv4
            ).network

            # next-hop = adresa Router-ului pe legătura dintre Router și CSR (192.168.230.20)
            next_hop = str(ipaddress.IPv4Interface(
                tb.devices.Router.interfaces['GigabitEthernet0/2'].ipv4
            ).ip)

            # construim ruta
            route.device_attr[self.dev].vrf_attr['default'].address_family_attr['ipv4'] \
                .route_attr[str(dest_network)].next_hop_attr[next_hop].set_value(True)

            config = route.build_config(apply=False)
            self.dev.configure(config.cli_config.data)
            print(config)


if __name__ == '__main__':
    aetest.main()