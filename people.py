from db import DB

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

class People():
    def __init__(self):
        self.db = DB('people.db')
        self.table = 'people'
        self.db.create(self.table, scheme)
        data = self.db.get_data(self.table)
        if len(data) == 0:
            for data in initial_data:
                self.db.insert_data(self.table, data)

        self.methods = [
            {'name':'add', 'function': self.add},
            {'name':'delete', 'function': self.delete_by_id},
            {'name':'check', 'function': self.check},
            {'name':'exit', 'function': self.free},
            {'name':'get', 'function': self.get},
        ]

    def call_method_by_name(self, method_name, arg):
        for method in self.methods:
            if method_name == method['name']:
                if arg != None:
                    return method['function'](arg)
                else:
                    return method['function']()

    def add(self, data):
        self.db.insert_data(self.table, data)
        return self.db.get_data(self.table)

    def delete_by_id(self, id):
        self.db.delete_data(self.table, id)
        return self.db.get_data(self.table)

    def get(self):
        return self.db.get_data(self.table)

    def check(self, data):
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

    def free(self):
        self.db.close()
        return True