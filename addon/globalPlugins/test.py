# import globalPluginHandler
# from scriptHandler import script
# import ui
# import versionInfo

# class GlobalPlugin(globalPluginHandler.GlobalPlugin):

# 	@script(gesture="kb:NVDA+shift+v")
# 	def script_announceNVDAVersion(self, gesture):
# 		ui.message(versionInfo.version)

import globalPluginHandler
from scriptHandler import script
import tones # We want to hear beeps.
import api
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_doBeep(self, gesture):
			tones.beep(440, 1000)  # Beep a standard middle A for 1 second.
			
	__gestures = {
		"kb:NVDA+A": "doBeep"  # Assign the "NVDA+A" key combination to the doBeep method
	}