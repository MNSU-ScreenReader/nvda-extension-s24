
import appModuleHandler
import speech
from scriptHandler import script
import subprocess

def run_pylint(file_path):
    command = ['pylint', file_path]
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

class AppModule(appModuleHandler.AppModule):

    def script_announceLintErrors(self, gesture):
        # Hardcoded file path for testing
        filePath = "C:\Users\meron\PycharmProjects\pythonProject9\main.py"
        pylintOutput = run_pylint(filePath)
        errors = parse_pylint_output(pylintOutput)
        self.vocalize_errors(errors)

    def vocalize_errors(self, errors):
        if errors:
            for error in errors:
                speech.speak(f"Line {error['line']}, {error['type']}, {error['message']}")
        else:
            speech.speak("No linting errors.")

    __gestures = {
        "kb:NVDA+l": "announceLintErrors",
    }



   