import asyncio
import re
import sys
import time

from pyats import aetest, topology
from pyats.aetest.steps import Step

from lib.connectors.telnet_con import TelnetConnection

print(sys.path)


class ConfigureFDMManagement(aetest.Testcase):
    @aetest.test
    def load_testbed(self, steps):
        with steps.start("Load testbed"):
            self.tb = topology.loader.load('ftd_testbed.yaml')
            self.parent.parameters.update(tb=self.tb)

    @aetest.test
    def bring_up_router_interface(self, steps):
        for device in self.tb.devices:
            if self.tb.devices[device].type != 'ftd':
                continue
            with steps.start(f'Bring up management interface {device}', continue_=True) as step:  # type: Step

                for interface in self.tb.devices[device].interfaces:
                    if self.tb.devices[device].interfaces[interface].link.name != 'management':
                        continue

                    intf_obj = self.tb.devices[device].interfaces[interface]
                    conn_class = self.tb.devices[device].connections.get('telnet', {}).get('class', None)
                    assert conn_class, 'No connection for device {}'.format(device)
                    ip = self.tb.devices[device].connections.telnet.ip.compressed
                    port = self.tb.devices[device].connections.telnet.port
                    conn: TelnetConnection = conn_class(ip, port)

                    async def setup():
                        await conn.connect()
                        await asyncio.sleep(1)

                        conn.write("\n")
                        await asyncio.sleep(2)
                        out = await conn.read(n=2000)
                        print(out)

                        result = re.search(r'^\s*(?P<login>firepower login:)', out)
                        if not result:
                            step.skipped(reason='Configuration not required')

                        if result and result.group('login'):
                            conn.write("admin\n")
                            await asyncio.sleep(1)
                            conn.write("Admin123\n")
                            await asyncio.sleep(1)
                            out = await conn.read(n=2000)

                        # EULA
                        if "EULA:" in out:
                            conn.write("\n")
                            await asyncio.sleep(1)

                            while True:
                                out = await conn.read(n=2000)
                                if "--More--" in out:
                                    conn.write(" ")
                                elif "AGREE" in out:
                                    conn.write("YES\n")
                                    await asyncio.sleep(1)
                                    out = await conn.read(n=2000)
                                    break
                                else:
                                    break

                        # New password
                        if "Enter new password:" in out:
                            pw = self.tb.devices[device].credentials.default.password.plaintext
                            conn.write(pw + "\n")
                            await asyncio.sleep(1)
                            out = await conn.read(n=2000)

                        if "Confirm new password:" in out:
                            pw = self.tb.devices[device].credentials.default.password.plaintext
                            conn.write(pw + "\n")
                            await asyncio.sleep(1)
                            out = await conn.read(n=2000)

                        # IPv4
                        if "IPv4? (y/n) [y]:" in out:
                            conn.write("\n")
                            await asyncio.sleep(1)
                            out = await conn.read(n=2000)

                        if "IPv6? (y/n) [n]:" in out:
                            conn.write("\n")
                            await asyncio.sleep(1)
                            out = await conn.read(n=2000)

                        if "(dhcp/manual) [manual]:" in out:
                            conn.write("\n")
                            await asyncio.sleep(1)
                            out = await conn.read(n=2000)

                        if "Enter an IPv4 address" in out:
                            conn.write(intf_obj.ipv4.ip.compressed + "\n")
                            await asyncio.sleep(1)
                            out = await conn.read(n=2000)

                        if "Enter an IPv4 netmask" in out:
                            conn.write(intf_obj.ipv4.netmask.exploded + "\n")
                            await asyncio.sleep(1)
                            out = await conn.read(n=2000)

                        if "default gateway" in out:
                            conn.write((intf_obj.ipv4.ip + 1).compressed + "\n")
                            await asyncio.sleep(1)
                            out = await conn.read(n=2000)

                        if "DNS servers" in out:
                            conn.write("\n")
                            await asyncio.sleep(1)
                            out = await conn.read(n=2000)

                        if "search domains" in out:
                            conn.write("\n")
                            await asyncio.sleep(1)
                            out = await conn.read(n=2000)

                        if "locally? (yes/no) [yes]:" in out:
                            conn.write("\n")
                            await asyncio.sleep(1)
                            out = await conn.read(n=2000)

                        print("Final output:", out)

                    asyncio.run(setup())



class ConfigureInterfaces(aetest.Testcase):

    @aetest.setup
    def configure(self):
        tb = self.parent.parameters['tb']
        conn = tb.devices.IOU1.connections.telnet['class']
        print(conn)


if __name__ == '__main__':
    aetest.main()
