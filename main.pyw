from dialog import Dialog
from helper import Helper

_dialog = None

def _gui_event_listner(event, id, event_data):
    global _dialog
    if event == 'click':
        _dialog.set_active_tab(id)

    elif event == 'key':
        print('key', id)
        pass

ID_TAB_DB = Helper.random_id()
ID_TAB_EDITOR = Helper.random_id()
ID_TAB_ABOUT = Helper.random_id()

def _gui():
    global _dialog
    _dialog = Dialog()
    template = f'''
    size, XXL, 0, 0
    header, 🚀PEOPLE&DB, 1
    toolbar, 0, 0, 0
    tab, DB, {ID_TAB_DB}, 0
    xlabel, database, 0, 0
    treeview, , 999, name, age
    button, add, 0, 0
    button, delete, 0, 0
    separator, 0, 0, 0

    tab, ED, {ID_TAB_EDITOR}, 1
    xlabel, editor, 0, 0
    label, firstname, 998, 0
    input, qwe, 998, 0
    slabel, error, 0, 0
    separator, 0, 0, 0

    label, lastname, 998, 0
    input, qwe, 998, 0
    slabel, error, 0, 0
    separator, 0, 0, 0

    label, age, 998, 0
    input, qwe, 998, 0
    slabel, error, 0, 0
    separator, 0, 0, 0

    button, save, 0, 0

    tab, ??, {ID_TAB_ABOUT}, 2 
    xlabel, about, 0, 0

    button, osdfsdfk, 998, 2
    '''
    _dialog.template(template)
    _dialog.set_event_listner(_gui_event_listner)
    data = []
    for _ in range(200):
        data.append([Helper.random_name(), Helper.random_age()])
    _dialog.set_data_to_treeview(999, data)    
    _dialog.run()


def tests():
    _gui()
    #app = App()
    #app.run()

tests()