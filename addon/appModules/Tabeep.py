# TabBeep.py

import appModuleHandler
import tones
import api
import controlTypes

class AppModule(appModuleHandler.AppModule):

    def event_gainFocus(self, obj, nextHandler):
        # Subscribe to the key event
        obj.treeInterceptorManager.addTreeInterceptor(self.treeInterceptor)

        # Call the next handler in the focus chain
        nextHandler()

    def event_loseFocus(self, obj, nextHandler):
        # Unsubscribe from the key event
        obj.treeInterceptorManager.removeTreeInterceptor(self.treeInterceptor)

        # Call the next handler in the focus chain
        nextHandler()

    def script_tab_key(self, gesture):
        # Beep when the tab key is pressed
        tones.beep(1000, 200)
        api.performGesture("kb:Tab")

    def define_script(self, script, scriptList):
        scriptList.append(script)

    def __init__(self, *args, **kwargs):
        super(AppModule, self).__init__(*args, **kwargs)
        self.treeInterceptor = TreeInterceptor()

class TreeInterceptor(api.TreeInterceptor):
    def interceptTree(self, tree, availableCommands):
        # Define the command for the tab key
        availableCommands.append({
            'input': 'Tab',
            'script': 'script_tab_key',
            'func': lambda gesture: True,
            'obj': None,
            'commandName': 'tab_key',
            'displayName': 'Tab key',
            'gesture': 'kb:Tab',
            'description': 'Beep on Tab key press',
            'type': controlTypes.STATE_SYSTEM_NORMAL,
        })
        return True
