from pyats import aetest, topology

from lib.connectors.ssh_conn import SshConnection


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def load_testbed(self, steps):
        with steps.start("Load testbed"):
            tb = topology.loader.load('new_testbed.yaml')
            self.parent.parameters.update(tb=tb)


class ConfigureGenie(aetest.Testcase):
    @aetest.setup
    def connect(self, steps):
        tb = self.parent.parameters.get("tb")
        conn: SshConnection = tb.devices.RouterCSR.connections.ssh['class'](
            host=str(tb.devices.CSR.connections.ssh['ip']),
            port=str(tb.devices.CSR.connections.ssh['port']),
            username=tb.devices.CSR.connections.ssh.credentials.default['username'],
            password=tb.devices.CSR.connections.ssh.credentials.default['password'].plaintext,
        )
        conn.connect()
        conn.configure()


if __name__ == '__main__':
    aetest.main()
