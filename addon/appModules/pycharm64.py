import appModuleHandler
import tones
import api
import controlTypes
import speech
from scriptHandler import script
import subprocess

def run_pylint(file_path):
    command = ['pylint', file_path, 'C:\Users\meron\PycharmProjects\pythonProject9\main.py']
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout  
    except subprocess.CalledProcessError as e:
        return e.output
def parse_pylint_output(output):
    errors = []
    for line in output.split('\n'):
        if ":" in line and " " in line:
            parts = line.split(":", 3)
            if len(parts) >= 4:
                errors.append({
                    'line': parts[1],
                    'type': parts[2].strip(),
                    'message': parts[3].strip(),
                })
    return errors

def vocalize_errors(errors):
    if errors:
        for error in errors:
            speech.speakText(error)
    else:
        speech.speakText("No errors found.")

class AppModule(appModuleHandler.AppModule):
    
    def script_announceLintErrors(self, gesture):
        filePath = self.getActiveFilePath()  
        pylintOutput = run_pylint(filePath)
        errors = parse_pylint_output(pylintOutput)
        if errors:
            for error in errors:
                speech.speak(f"Line {error['line']}, {error['type']}, {error['message']}")
        else:
            speech.speak("No linting errors.")

    __gestures = {
        "kb:NVDA+l": "announceLintErrors",
    }



   