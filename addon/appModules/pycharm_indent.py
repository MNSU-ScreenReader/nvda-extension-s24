import tones
import api
import speech
import appModuleHandler

class PyCharmAppModule(appModuleHandler.AppModule):
    def event_gainFocus(self, obj, nextHandler):
        # Play a beep sound when focus changes
        import tones
        tones.beep(550, 50)
        nextHandler()

    def script_speakCurrentLine(self, gesture):
        try:
            # Check if PyCharm window is active
            if api.getForegroundObject().windowClassName == "SunAwtFrame":  # Check for PyCharm window class name
                # Get the focused object
                focusedObject = api.getFocusObject()

                # If focused object is a text area, get the current line content
                if focusedObject.role == api.ROLE_EDITABLETEXT:
                    currentLine = focusedObject.value.split('\n')[focusedObject.caretOffset.y]
                    speech.speakText(currentLine)
                else:
                    # If not in a text area, announce the object role
                    speech.speakText("Focused object is " + focusedObject.role)
            else:
                # If PyCharm window is not active, do nothing
                pass
        except AttributeError:
            speech.speakText("No text found")

    __gestures = {
        "kb:NVDA+A": "speakCurrentLine"
    }
