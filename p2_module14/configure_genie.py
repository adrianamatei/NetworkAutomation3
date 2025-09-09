from pyats import aetest,topology
from genie.libs.conf.interface.iosxe import Interface

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def load_testbed(self, steps):
        with steps.start("Load testbed"):
            tb = topology.loader.load('testbed2.yaml')
            self.parent.parameters.update(tb=tb)
class ConfigureGenie(aetest.Testcase):
    @aetest.setup
    def