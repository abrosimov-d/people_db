from dialog import Dialog
from helper import Helper

ID_BUTTON_YES = Helper.random_id()
ID_BUTTON_NO = Helper.random_id()

class YesNoDialog(Dialog):
    def __init__(self, parent, title, message):
        super().__init__(parent)
        template = f'''
            size, L, 0, 0
            separator, 0, 0, 0
            label, {title}, 0, 0
            label, {message}, 0, 0
            button, yes, {ID_BUTTON_YES}, 0, 0
            button, no, {ID_BUTTON_NO}, 0, 0
        '''
        super().template(template)
        super().set_event_listener(self.__event_listener)
        self.result = 0

    def show(self):
        super().run()
        return self.result

    def __event_listener(self, event, id, event_data):
        if event == 'init':
            pass

        if event == 'click' and id == ID_BUTTON_YES:
            self.result = 1
            super().close_window()

        if event == 'click' and id == ID_BUTTON_NO:
            super().close_window()

        if event == 'close':
            return True