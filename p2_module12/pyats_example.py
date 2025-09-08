import asyncio
import subprocess
import ipaddress
import multiprocessing
import time

from pyats import aetest, topology
import yaml

from lib.connectors.rest_con import RESTConnector
from lib.connectors.telnet_con import TelnetConnection
import p2_module12.ssh_config
from p2_module12 import ssh_config


# with open("testbed.yaml", "r") as yaml_file:
#     data = yaml.load(yaml_file)
#     print(data)

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def load_testbed(self, steps):
        with steps.start("Load testbed"):
            self.tb = topology.loader.load('new_testbed.yaml')
            # dev=self.tb.devices.IOU1
            # dev=self.tb.devices['IOU1']
            # print(self.tb)
            self.parent.parameters.update(tb=self.tb)


    @aetest.subsection
    def bring_up_server_interface(self, steps):
        server = self.tb.devices['UbuntuServer']
        for interface in server.interfaces:
            intf = server.interfaces[interface]
            with steps.start("Bring up interface {interface.name}"):
                subprocess.run(['sudo', 'ip', 'addr', 'add', f'{intf.ipv4}', 'dev', f'{interface}'])
                subprocess.run(['sudo', 'ip', 'link', 'set', 'dev', f'{interface}', 'up'])

        with steps.start("Add routes"):
            for device in self.tb.devices:
                if self.tb.devices[device].type!='router':
                    continue
                gateway = self.tb.devices[device].interfaces['initial'].ipv4.compressed
                for interface in self.tb.devices[device].interfaces:
                    if self.tb.devices[device].interfaces[interface].link.name=='management':
                        continue
                    subnet = self.tb.devices[device].interfaces[interface].ipv4.network.compressed
                    print(subnet)

                    subprocess.run(
                        ['sudo', 'ip', 'route', 'add', f'{subnet}', 'via', f'{gateway}', 'metric'])

                #print(device)

    @aetest.subsection
    def bring_up_server_interface(self, steps):
        for device in self.tb.devices:
            if self.tb.devices[device].type != 'router':
                continue
            with steps.start(f'Bring up interface {device}',continue_=True):

                for interface in self.tb.devices[device].interfaces:
                    if self.tb.devices[device].interfaces[interface].link.name !='management':
                        continue

                    intf_obj=self.tb.devices[device].interfaces[interface]
                    conn_class=self.tb.devices[device].connections.get('telnet',{}).get('class',None)
                    assert conn_class,'No connection for device {}'.format(device)
                    ip = self.tb.devices[device].connections.telnet.ip.compressed
                    port = self.tb.devices[device].connections.telnet.port
                    q=multiprocessing.Queue()

                    commands=ssh_config.commands
                    formatted_commands=list(map(
                        lambda s: s.format(
                            interface=interface,
                            ip=intf_obj.ipv4.ip.compressed,
                            sm=intf_obj.ipv4.netmask.exploded,
                            hostname=device,
                            domain=self.tb.devices[device].custom.get('domain',''),
                            username=self.tb.devices[device].connections.telnet.credentials.login.username,
                            password=self.tb.devices[device].connections.telnet.credentials.login.password,

                        ),
                        commands
                    ))

                    conn: TelnetConnection = conn_class(ip, port)


                    async def setup():
                        await conn.connect()
                        time.sleep(1)
                        await conn.execute_commends(formatted_commands, '#')
                    asyncio.run(setup())
    @aetest.subsection
    def connect_via_rest(self,steps):
        for device in self.tb.devices:
            if self.tb.devices[device].type != 'router':
                continue
            if 'rest' not in self.tb.devices[device].connections:
                continue


            for interface in self.tb.devices[device].interfaces:
                if self.tb.devices[device].interfaces[interface].link.name !='management':
                    continue
                conn_class: RESTConnector=self.tb.devices[device].connections['rest']['class']
                conn_data=self.tb.devices[device].connections['rest']
                conn_obj=conn_class(
                    ip=conn_data.ip.compressed,
                    port=conn_data['port'],
                    username=conn_data['username'],
                    password=conn_data['password'],
                )






class ConfigureInterfaces(aetest.Testcase):

    @aetest.setup
    def configure(self):
        tb = self.parent.parameters['tb']
        conn = tb.devices['IOU1'].connections.telnet['class']
        print(conn)


if __name__ == '__main__':
    aetest.main()

