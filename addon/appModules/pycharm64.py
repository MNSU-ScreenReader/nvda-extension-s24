import appModuleHandler
import tones
import api
import controlTypes

class AppModule(appModuleHandler.AppModule):

    def event_gainFocus(self, obj, nextHandler):
        tones.beep(550, 50)
        nextHandler()
   
    def event_caret(self, obj, nextHandler):
        current_line_text = self.get_current_line_text(obj)
        if current_line_text is not None:  
         indentation_level = self.get_indentation_level(current_line_text)
         self.announce_indentation(indentation_level)
        nextHandler()

    def get_current_line_text(self, obj):
        pass

    def get_indentation_level(self, line_text):
        indentation_level = len(line_text) - len(line_text.lstrip(' '))
        return indentation_level // 4

    def announce_indentation(self, level):
        if level > 0:
            tones.beep(440 + (level * 20), 100)
        else:
            pass
