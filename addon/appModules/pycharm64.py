import appModuleHandler
import tones
import api
import controlTypes
import speech
from scriptHandler import script

class AppModule(appModuleHandler.AppModule):

    def event_gainFocus(self, obj, nextHandler):
        tones.beep(550, 50)
        nextHandler()
    
    def script_boopOnTab(self, gesture):
        focusObj = api.getFocusObject()
        if isinstance(focusObj, NVDAObjects.IAccessible.IAccessible) and focusObj.role == controlTypes.Role.EDITABLETEXT:
            tones.beep(440, 100)  
        gesture.send()
   
    def script_reportIndentation(self, gesture):
        obj = api.getNavigatorObject()
        try:
            textInfo = obj.makeTextInfo(textInfos.POSITION_CARET)
            textInfo.expand(textInfos.UNIT_CHARACTER)
            text = textInfo.text
        except (RuntimeError, NotImplementedError):
            gesture.send()
            return
        if text == " ":
            speech.speak("indentation")
        else:
            speech.speak(text)

    def __init__(self, *args, **kwargs):
        super(AppModule, self).__init__(*args, **kwargs)
        self.bindGesture("kb:space", "reportIndentation")
   

  