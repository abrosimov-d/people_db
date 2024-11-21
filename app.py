from helper import Helper
from db.db import DB
from peopledialog import PeopleDialog

initial_data = [
    {"firstname": "Иван", "lastname": "Иванов", "age": 30},
    {"firstname": "Мария", "lastname": "Петрова", "age": 25},
    {"firstname": "Алексей", "lastname": "Сидоров", "age": 40}
]

scheme = {
    'id': 'integer primary key autoincrement not null',
    'firstname': 'text',
    'lastname': 'text',
    'age': 'integer'
}

class App():
    def __init__(self):
        self.db = DB('people.db')
        self.table = 'people'
        self.db.create(self.table, scheme)
        data = self.db.get_data(self.table)
        if len(data) == 0:
            for data in initial_data:
                self.db.insert_data(self.table, data)
        self.dialog = PeopleDialog(self.on_event_listener)

    def on_event_listener(self, event):
        if 'action' in event:
            if event['action'] == 'add':
                self.db.insert_data(self.table, event['data'])
            
            elif event['action'] == 'dropall':
                self.db.drop_table(self.table)
                self.db.create(self.table, scheme)
            
            elif event['action'] == 'check':
                data = event['data']
                errors = []
                if not len(data['firstname']):
                    errors.append('wrong firstname')
                if not len(data['lastname']):
                    errors.append('wrong lastname')
                try:
                    age = int(data['age'])
                    if age < 0 or age > 150:
                        errors.append('wrong age')
                except:
                    errors.append('wrong age')
                if len(errors):
                    data['error'] = ', '.join(errors)
                return data
            
            elif event['action'] == 'exit':
                self.db.close()
                return True

        return self.db.get_data(self.table)