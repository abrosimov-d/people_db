from dialog import Dialog
from helper import Helper

ID_BUTTON_ADD = Helper.random_id()
ID_TREVIEW_PEOPLE = Helper.random_id()
ID_BUTTON_DELETE = Helper.random_id()
ID_BUTTON_DROPALL = Helper.random_id()
ID_BUTTON_SAVE = Helper.random_id()
ID_INPUT_FIRSTNAME = Helper.random_id()
ID_INPUT_LASTNAME = Helper.random_id()
ID_INPUT_AGE = Helper.random_id()
ID_BUTTON_RANDOM = Helper.random_id()
ID_LABEL_ERROR = Helper.random_id()

class PeopleDialog(Dialog):
    def __init__(self, on_event_listener):
        super().__init__(None)
        self.__on_event_listener = on_event_listener

        template = f'''
        size, XXL, 0, 0
        header, 🚀PEOPLE_DB, 0, 0
        tab, DB, 0, 0
        button, add, {ID_BUTTON_ADD}, 0
        button, delete, {ID_BUTTON_DELETE}, 0        
        button, drop table, {ID_BUTTON_DROPALL}, 0
        treeview, 0, {ID_TREVIEW_PEOPLE}, id, firstname, lastname, age
        
        tab, ED, 0, 1
        label, firstname:, 0, 0
        input,, {ID_INPUT_FIRSTNAME}, 0
        separator, 0, 0, 0

        label, lastname:, 0, 0
        input,, {ID_INPUT_LASTNAME}, 0
        separator, 0, 0, 0

        label, age:, 0, 0
        input,, {ID_INPUT_AGE}, 0
        separator, 0, 0, 0
       
        separator, 0, 0, 0
       
        button, fill random, {ID_BUTTON_RANDOM}, 0  
        button, cancel, {ID_BUTTON_SAVE}, 0  
        slabel,,{ID_LABEL_ERROR},0
 
        tab, AB, 0, 2
        xlabel, PEOPLE_DB, 0, 0
        label, final assignment for python course, 0, 0
        label, used: tkinter • sqlite3, 0, 0 
        label, date: XX.11.2024, 0, 0
        urlpyt  button, https://github.com/abrosimov-d/people_db, 0, 0

'''
        super().template(template)
        super().set_event_listener(self.__event_listener)
        super().run()
    
    def __event_listener(self, event, id, event_data):

        if event == 'init':
            event = {}
            data = self.__on_event_listener(event)
            self.set_data_to_treeview(ID_TREVIEW_PEOPLE, data)
            self.set_enable_by_id(ID_BUTTON_DELETE, False)
        
        if event == 'click' and id == ID_BUTTON_ADD:
            self.set_active_tab(1)

        if event == 'click' and id == ID_BUTTON_DROPALL:
            event = {}
            event['action'] = 'dropall'
            data = self.__on_event_listener(event)
            self.set_data_to_treeview(ID_TREVIEW_PEOPLE, data)

        if event == 'click' and id == ID_BUTTON_SAVE:
            event = {}
            event['action'] = 'check'
            data = {}
            data['firstname'] = self.get_text_by_id(ID_INPUT_FIRSTNAME)
            data['lastname'] = self.get_text_by_id(ID_INPUT_LASTNAME)
            data['age'] = self.get_text_by_id(ID_INPUT_AGE)
            event['data'] = data
            data = self.__on_event_listener(event)
            if 'error' not in data:
                event['action'] = 'add'
                data = self.__on_event_listener(event)
                self.set_data_to_treeview(ID_TREVIEW_PEOPLE, data)
            else:
                self.set_text_by_id(ID_LABEL_ERROR, data['error'])
            self.set_active_tab(0)

        if event == 'click' and id == ID_BUTTON_RANDOM:
            firtsname, lastname = Helper.random_name().split(' ')
            age = Helper.random_age()
            self.set_text_by_id(ID_INPUT_FIRSTNAME, firtsname)
            self.set_text_by_id(ID_INPUT_LASTNAME, lastname)
            self.set_text_by_id(ID_INPUT_AGE, str(age))

        if event == 'tab' and id == 1:
            self.set_text_by_id(ID_INPUT_FIRSTNAME, '')
            self.set_text_by_id(ID_INPUT_LASTNAME, '')
            self.set_text_by_id(ID_INPUT_AGE, '')

        if event == 'key':
            event = {}
            event['action'] = 'check'
            data = {}
            data['firstname'] = self.get_text_by_id(ID_INPUT_FIRSTNAME)
            data['lastname'] = self.get_text_by_id(ID_INPUT_LASTNAME)
            data['age'] = self.get_text_by_id(ID_INPUT_AGE)
            event['data'] = data
            data = self.__on_event_listener(event)
            if 'error' not in data:
                self.set_text_by_id(ID_LABEL_ERROR, '')
                self.set_text_by_id(ID_BUTTON_SAVE, 'save')
            else:
                self.set_text_by_id(ID_LABEL_ERROR, data['error'])
                self.set_text_by_id(ID_BUTTON_SAVE, 'cancel')

        if event == 'close':
            event = {}
            event['action'] = 'exit'
            return self.__on_event_listener(event)
        
        if event == 'select':
            if event_data != None:
                self.set_text_by_id(ID_BUTTON_DELETE, f'delete {event_data[1]} {event_data[2]} ({event_data[3]})')
            else:
                self.set_text_by_id(ID_BUTTON_DELETE, 'delete')
            self.set_enable_by_id(ID_BUTTON_DELETE, event_data != None)

        if event == 'click' and id == ID_BUTTON_DELETE:
            event = {}
            data = {}
            event['action'] = 'delete'
            event['data'] = self.get_item_selected(ID_TREVIEW_PEOPLE)
            data = self.__on_event_listener(event)
            self.set_data_to_treeview(ID_TREVIEW_PEOPLE, data)
