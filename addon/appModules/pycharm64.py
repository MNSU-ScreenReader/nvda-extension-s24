import appModuleHandler
import tones
import api
import controlTypes

class AppModule(appModuleHandler.AppModule):

    def event_gainFocus(self, obj, nextHandler):
        tones.beep(550, 50)
        nextHandler()

    def event_stateChange(self, obj, nextHandler):
        
        if obj.role == controlTypes.ROLE_EDITABLETEXT and obj.states:
           
            tones.beep(660, 50)
        nextHandler()
