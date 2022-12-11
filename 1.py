import ZeekControl.plugin
import ZeekControl.cmdresult

class test(ZeekControl.plugin.Plugin):
    def __init__(self):
        super(test, self).__init__(apiversion=1)

    def name(self):
        return "test"

    def prefix(self):
        return "test"

    def pluginVersion(self):
        return 1

    def options(self):
        return [("foo", "int", 1, "Just a test option."),
                ("enabled", "bool", False, "Set to enable plugin")]

    def commands(self):
        return [("bar", "", "A test command from the Test plugin.")]

    def cmd_check_pre(self, nodes):
        self.message("test: Test pre 'check':  %s" % self._nodes(nodes))

    def cmd_check_post(self, results):
        self.message("test: Test post 'check': %s" % self._results(results))
