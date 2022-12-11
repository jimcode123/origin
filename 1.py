import ZeekControl.plugin
import ZeekControl.cmdresult

class test(ZeekControl.plugin.Plugin):
    def __init__(self):
        super(test, self).__init__(apiversion=1)

    def name(self):
        return "test"

    def pluginVersion(self):
        return 1

