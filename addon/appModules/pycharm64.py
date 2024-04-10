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

class IndentationParser:

    def __init__(self, prgm_text: str):
        self.prgm_text: str = prgm_text

    def get_prgm_text(self):
        print(self.prgm_text, "hoe ass")
        return self.prgm_text

    def get_indentation(self):
        indentation_percentages, majority_indentation = self.get_indentation_statistics()
        indentation = 0
        count = 0
        lines = self.prgm_text.split('\n')

        for idx, line in enumerate(lines, start=1):
            if line.strip():  # Non-empty line
                current_indentation = len(line) - len(line.lstrip())
                if current_indentation > 0:
                    count += 1
                    indentation = current_indentation
                    
                    
                    if current_indentation % majority_indentation != 0:
                        if lines[idx - 2].strip().endswith(','):
                            continue
                        print("error line:", idx, " change to", majority_indentation)
                        return majority_indentation, idx
        return indentation, idx
    
    def get_indentation_statistics(self):
        indentation_count = {}
        total_lines = 0
        temp = 9999999
        lines = self.prgm_text.split('\n')

        for line in lines:
            if line.strip():  # Non-empty line
                current_indentation = len(line) - len(line.lstrip())

                if current_indentation > 0 and current_indentation < (2 * temp):
                    indentation_count[current_indentation] = indentation_count.get(current_indentation, 0) + 1
                    total_lines += 1
                    temp = current_indentation

        if not indentation_count:
            return {}

        indentation_percentages = {indent: count / total_lines * 100 for indent, count in indentation_count.items()}
        majority_indentation = max(indentation_percentages, key=indentation_percentages.get)
        return indentation_percentages, majority_indentation

class AppModule(appModuleHandler.AppModule):
    def __init__(self, pid, appName=None):
        super(AppModule, self).__init__(pid, appName)


    def chooseNVDAObjectOverlayClasses(self, obj, clsList):
        if obj.role == controlTypes.ROLE_EDITABLETEXT:
            print("In the editor")
            clsList.insert(0, PyCharmEditWindow)



class PyCharmEditWindow(EditWindowBaseCls, EditableTextWithSuggestions):
    code_string = ""
    def event_gainFocus(self):
        super(PyCharmEditWindow, self).event_gainFocus()
        self.appModule.edit = None
        self.appModule._edit = weakref.ref(self)

    def event_caret(self):
        super(PyCharmEditWindow, self).event_caret()
        tones.beep(330,50)
        info = self.makeTextInfo(textInfos.POSITION_ALL)
        code_string = info.text
        #print(code_string)
        parser = IndentationParser(code_string)
        temp, _ = parser.get_indentation()
        print("Indentation used in the program:", temp)
        speech.speakText(f'Indentation is {temp}') 
        indentation_percentages, majority_indentation = parser.get_indentation_statistics()
        print(indentation_percentages)