from pyats import aetest, topology
import subprocess
from pyats.datastructures import AttrDict
import sys
# from lib.connectors.ssh_conn import SshConnection
# from lib.connectors.telnet_con import TelnetConnection

obj = AttrDict()
print(sys.path)


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def load_testbed(self, steps):
        with steps.start('Load testbed'):
            self.tb = topology.loader.load('new_testbed.yaml')
            self.parent.parameters.update(tb=self.tb)

    @aetest.subsection
    def bring_up_server_interface(self, steps):
        server = self.tb.devices['UbuntuServer']
        for intf_name, intf in server.interfaces.items():
            # intf = server.interfaces[interface]
            with steps.start(f'Bring up interface {intf_name}'):
                subprocess.run(['sudo', 'ip', 'addr', 'add', f'{intf.ipv4}', 'dev', f'{intf_name}'])
                subprocess.run(['sudo', 'ip', 'link', 'set', 'dev', f'{intf_name}', 'up'])

        with steps.start('Add routes'):
            for device in self.tb.devices:
                if self.tb.devices[device].type != 'router':
                    continue
                gateway = self.tb.devices[device].interfaces['initial'].ipv4.ip.compressed
                for interface in self.tb.devices[device].interfaces:
                    if self.tb.devices[device].interfaces[interface].link.name == 'management':
                        continue
                    subnet = self.tb.devices[device].interfaces[interface].ipv4.network.compressed
                    subprocess.run(['sudo', 'ip', 'route', 'add', f'{subnet}', 'via', f'{gateway}'])

                # print(device)


if __name__ == '__main__':
    aetest.main()
