import ZeekControl.plugin
from ZeekControl import config

class Foo(ZeekControl.plugin.Plugin):
    def __init__(self):
        super(Foo, self).__init__(apiversion=1)

    def name(self):
        return "foo"

    def pluginVersion(self):
        return 1

    def init(self):
        self.message("foo plugin is initialized")
        return True
