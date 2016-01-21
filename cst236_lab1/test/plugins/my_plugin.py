from nose2.events import Plugin
from ReqTracer import Requirements

class MyPlugin(Plugin):
    configSection = 'req-tracer'
    commandLineSwitch = (None, 'hello-world', 'Say hello!')

    def afterSummaryReport(self, event):
        with open("TraceOutput.txt", 'w') as  w:
            for key, item in sorted(Requirements.items()):
                w.write(key + ':' + str(item.func_name) + '\n')