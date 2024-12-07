from peopledialog import PeopleDialog
from people import People

class App():
    def __init__(self):
        self.people = People()
        self.dialog = PeopleDialog(self.on_event_listener)

    def on_event_listener(self, event):
        return self.people.call_method_by_name(event['action'], event['data'])