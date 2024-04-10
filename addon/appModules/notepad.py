import appModuleHandler
import speech
import api
class AppModule(appModuleHandler.AppModule):
	def event_gainFocus(self, obj, nextHandler):
		import tones
		tones.beep(550, 50)
		nextHandler()
		
	def script_doSpeak(self, gesture):
		try:
			focusedObject = api.getFocusObject()
			text = focusedObject.value
			speech.speakText(text)
		except AttributeError:
			speech.speakText("No text Found")
		

	__gestures={
		"kb:NVDA+A": "doSpeak"
	}