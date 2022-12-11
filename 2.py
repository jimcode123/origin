import ZeekControl.plugin
import ZeekControl.cmdresult

class TestPlugin2(ZeekControl.plugin.Plugin):
    def __init__(self):
        super(TestPlugin2, self).__init__(apiversion=1)

    def name(self):
        return "TestPlugin2"

    def prefix(self):
        return "test"

    def pluginVersion(self):
        return 1

    def init(self):
        if not self.getOption("enabled"):
            return False

        foo = self.getOption("foo")

        self.message("TestPlugin2: Test initialized")
        self.message("TestPlugin2: The value of foo is: %s" % foo)
        self.message("TestPlugin2: The current value of bar is: %s" % self.getState("bar"))

        for n in self.nodes():
            try:
                self.message("TestPlugin2: mykey is: %s" % n.test_mykey)
            except AttributeError:
                self.message("TestPlugin2: mykey is not set")

        for h in self.hosts():
            self.message("TestPlugin2: host %s" % h.host)

        return True

    def options(self):
        return [("foo", "int", 1, "Just a test option."),
                ("enabled", "bool", False, "Set to enable plugin")]

    def commands(self):
        return [("bar", "", "A test command from the Test plugin.")]

    def nodeKeys(self):
        return ["mykey"]

    def zeekctl_config(self):
        script = "# This is a test."
        return script

    def done(self):
        self.message("TestPlugin2: done")

    def _nodes(self, nodes):

        if not nodes:
            return "<empty>"

        if isinstance(nodes[0], tuple):
            nodes = [n[0] for n in nodes]

        return ",".join([str(n) for n in nodes])

    def _results(self, results):

        if not results:
            return "<empty>"

        return ",".join(["%s/%s" % (str(n[0]), n[1]) for n in results])

    def zeekProcessDied(self, node):
        self.message("TestPlugin2: Zeek process died for %s" % node)

    def hostStatusChanged(self, host, status):
        self.message("TestPlugin2: host status changed: %s -> %s" % (host, status))

    def cmd_custom(self, cmd, args, cmdout):
        results = ZeekControl.cmdresult.CmdResult()

        bar = self.getState("bar")
        if not bar:
            bar = 1

        self.setState("bar", bar + 1)
        self.message("TestPlugin2: My command: %s" % args)

        return results

    def cmd_check_pre(self, nodes):
        self.message("TestPlugin2: Test pre 'check':  %s" % self._nodes(nodes))

    def cmd_check_post(self, results):
        self.message("TestPlugin2: Test post 'check': %s" % self._results(results))

    def cmd_nodes_pre(self):
        self.message("TestPlugin2: Test pre 'nodes'")
        return True

    def cmd_nodes_post(self):
        self.message("TestPlugin2: Test post 'nodes'")

    def cmd_config_pre(self):
        self.message("TestPlugin2: Test pre 'config'")
        return True

    def cmd_config_post(self):
        self.message("TestPlugin2: Test post 'config'")

    def cmd_deploy_pre(self):
        self.message("TestPlugin2: Test pre 'deploy'")
        return True

    def cmd_deploy_post(self):
        self.message("TestPlugin2: Test post 'deploy'")

    def cmd_exec_pre(self, cmdline):
        self.message("TestPlugin2: Test pre 'exec':  %s" % cmdline)
        return True

    def cmd_exec_post(self, cmdline):
        self.message("TestPlugin2: Test post 'exec': %s" % cmdline)

    def cmd_install_pre(self):
        self.message("TestPlugin2: Test pre 'install'")
        return True

    def cmd_install_post(self):
        self.message("TestPlugin2: Test post 'install'")

    def cmd_cron_pre(self, arg, watch):
        self.message("TestPlugin2: Test pre 'cron':  %s/%s" % (arg, watch))
        return True

    def cmd_cron_post(self, arg, watch):
        self.message("TestPlugin2: Test post 'cron': %s/%s" % (arg, watch))

    def cmd_restart_pre(self, nodes, clean):
        self.message("TestPlugin2: Test pre 'restart':  %s (%s)" % (self._nodes(nodes), clean))

    def cmd_restart_post(self, nodes):
        self.message("TestPlugin2: Test post 'restart': %s" % self._nodes(nodes))

    def cmd_start_pre(self, nodes):
        self.message("TestPlugin2: Test pre 'start':  %s" % self._nodes(nodes))

    def cmd_start_post(self, results):
        self.message("TestPlugin2: Test post 'start': %s" % self._results(results))

    def cmd_stop_pre(self, nodes):
        self.message("TestPlugin2: Test pre 'stop':  %s" % self._nodes(nodes))

    def cmd_stop_post(self, results):
        self.message("TestPlugin2: Test post 'stop': %s" % self._results(results))

    def cmd_status_pre(self, nodes):
        self.message("TestPlugin2: Test pre 'status':  %s" % self._nodes(nodes))

    def cmd_status_post(self, nodes):
        self.message("TestPlugin2: Test post 'status': %s" % self._nodes(nodes))

    def cmd_update_pre(self, nodes):
        self.message("TestPlugin2: Test pre 'update':  %s" % self._nodes(nodes))

    def cmd_update_post(self, results):
        self.message("TestPlugin2: Test post 'update': %s" % self._results(results))

    def cmd_df_pre(self, nodes):
        self.message("TestPlugin2: Test pre 'df':  %s" % self._nodes(nodes))

    def cmd_df_post(self, nodes):
        self.message("TestPlugin2: Test post 'df': %s" % self._nodes(nodes))

    def cmd_diag_pre(self, nodes):
        self.message("TestPlugin2: Test pre 'diag':  %s" % self._nodes(nodes))

    def cmd_diag_post(self, nodes):
        self.message("TestPlugin2: Test post 'diag': %s" % self._nodes(nodes))

    def cmd_peerstatus_pre(self, nodes):
        self.message("TestPlugin2: Test pre 'peerstatus':  %s" % self._nodes(nodes))

    def cmd_peerstatus_post(self, nodes):
        self.message("TestPlugin2: Test post 'peerstatus': %s" % self._nodes(nodes))

    def cmd_netstats_pre(self, nodes):
        self.message("TestPlugin2: Test pre 'netstats':  %s" % self._nodes(nodes))

    def cmd_netstats_post(self, nodes):
        self.message("TestPlugin2: Test post 'netstats': %s" % self._nodes(nodes))

    def cmd_top_pre(self, nodes):
        self.message("TestPlugin2: Test pre 'top':  %s" % self._nodes(nodes))

    def cmd_top_post(self, nodes):
        self.message("TestPlugin2: Test post 'top': %s" % self._nodes(nodes))

    def cmd_cleanup_pre(self, nodes, all):
        self.message("TestPlugin2: Test pre 'cleanup':  %s (%s)" % (self._nodes(nodes), all))

    def cmd_cleanup_post(self, nodes, all):
        self.message("TestPlugin2: Test post 'cleanup': %s (%s)" % (self._nodes(nodes), all))

    def cmd_capstats_pre(self, nodes, interval):
        self.message("TestPlugin2: Test pre 'capstats':  %s (%d)" % (self._nodes(nodes), interval))

    def cmd_capstats_post(self, nodes, interval):
        self.message("TestPlugin2: Test post 'capstats':  %s (%d)" % (self._nodes(nodes), interval))

    def cmd_scripts_pre(self, nodes, check):
        self.message("TestPlugin2: Test pre 'scripts':  %s (%s)" % (self._nodes(nodes), check))

    def cmd_scripts_post(self, nodes, check):
        self.message("TestPlugin2: Test post 'scripts': %s (%s)" % (self._nodes(nodes), check))

    def cmd_print_pre(self, nodes, id):
        self.message("TestPlugin2: Test pre 'print':  %s (%s)" % (self._nodes(nodes), id))

    def cmd_print_post(self, nodes, id):
        self.message("TestPlugin2: Test post 'print': %s (%s)" % (self._nodes(nodes), id))

    def cmd_process_pre(self, trace, options, scripts):
        self.message("TestPlugin2: Test pre 'process': %s %s -- %s" % (trace, options, scripts))
        return True

    def cmd_process_post(self, trace, options, scripts, success):
        self.message("TestPlugin2: Test post 'process': %s %s -- %s -> %s" % (trace, options, scripts, success))
