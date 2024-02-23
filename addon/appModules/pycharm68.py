import globalPluginHandler
import tones
import keyboardHandler
from logHandler import log

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    def script_beepOnTab(self, gesture):
        if gesture.vkCode == keyboardHandler.VK_TAB:
            tones.beep(550, 50)
        else:
            gesture.send()

    def __init__(self, *args, **kwargs):
        super(GlobalPlugin, self).__init__(*args, **kwargs)
        self.bindGesture("kb:tab", "beepOnTab")
