import sys,os
import ast
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

editor_file = ""
current_idx = -1
class IndentationParser:
    def __init__(self, prgm_text: str):
        self.prgm_text: str = prgm_text

    def get_prgm_text(self):
        return self.prgm_text

    def get_indentation(self, current_line: str):
        indentation_percentages, majority_indentation = self.get_indentation_statistics()
        indentation = 0
        count = 0
        current_idx = -1
        lines = self.prgm_text.split('\n')

        for idx, line in enumerate(lines, start=1):
            if line.strip():  # Non-empty line
                current_indentation = len(line) - len(line.lstrip())
                if current_indentation > 0:
                    count += 1

                    if(current_line == line):
                        indentation = current_indentation
                        current_idx = idx

                    if current_indentation % majority_indentation != 0:
                        if lines[idx - 2].strip().endswith(','):
                            continue
                        print("error line:", idx, " change to", majority_indentation)
                        return majority_indentation, idx
        return indentation/majority_indentation, current_idx
    
    def get_indentation_statistics(self):
        indentation_count = {}
        total_lines = 0
        temp = sys.maxsize
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
    def event_gainFocus(self):
        super(PyCharmEditWindow, self).event_gainFocus()
        self.appModule.edit = None
        self.appModule._edit = weakref.ref(self)

    def event_caret(self):
        super(PyCharmEditWindow, self).event_caret()
        tones.beep(330,50)
        global editor_file
        info = self.makeTextInfo(textInfos.POSITION_ALL)
        info2 = self.makeTextInfo(textInfos.POSITION_CARET)

        #Stores the file that's in the editor
        editor_file = info.text
        info2.expand(textInfos.UNIT_LINE)
        
        #Gets the current line and indentation level of the caret
        current_line = info2.text.strip('\n')
        current = len(current_line) - len(current_line.lstrip())
        
        #Parses for the indentation level of the current line, dividing by majority to get the level
        parser = IndentationParser(editor_file)
        global current_idx
        indentation, current_idx = parser.get_indentation(current_line)
        #Reads aloud indentation level of current line
        speech.speakText(f'Indentation is {int(indentation)}') 
        indentation_percentages, majority_indentation = parser.get_indentation_statistics()

    def script_detectFunction(self,gesture):
        #print("Editor File:", editor_file)
        tree = ast.parse(editor_file)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Check if the current_idx is within the range of this function's lines
                if node.lineno <= current_idx:
                    function_name = node.name
        speech.speakText(f'In Function {function_name}')
    __gestures = {
        "kb:NVDA+I": "detectFunction",
    }
