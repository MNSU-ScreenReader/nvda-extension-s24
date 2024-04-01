import sys,os
import appModuleHandler
import eventHandler
import scriptHandler
import tones
import api
import ui
import controlTypes
import textInfos
import speech
import weakref
from queueHandler import registerGeneratorObject
from NVDAObjects.IAccessible import IAccessible
from editableText import EditableTextWithoutAutoSelectDetection
from NVDAObjects.behaviors import EditableTextWithAutoSelectDetection as EditWindowBaseCls
from NVDAObjects.behaviors import EditableTextWithSuggestions
parser = None
class AppModule(appModuleHandler.AppModule):
    def __init__(self, pid, appName=None):
        super(AppModule, self).__init__(pid, appName)
        
    def chooseNVDAObjectOverlayClasses(self, obj, clsList):
        if obj.role == controlTypes.ROLE_EDITABLETEXT:
            print("In the editor")
            clsList.insert(0, PyCharmEditWindow)

    

class PyCharmEditWindow(EditWindowBaseCls, EditableTextWithSuggestions):

    def event_gainFocus(self):
        super(PyCharmEditWindow, self).event_gainFocus()
        self.appModule.edit = None
        self.appModule._edit = weakref.ref(self)

    def event_caret(self):
        super(PyCharmEditWindow, self).event_caret()
        tones.beep(330,50)
        info = self.makeTextInfo(textInfos.POSITION_ALL)
        info.expand(textInfos.UNIT_LINE)

    