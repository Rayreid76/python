from datetime import datetime

class call(object):
    id = 0
    def __init__(self, name, phone_number, reason):
        self.unique_id = call.id
        self.name = name
        self.phone_number = phone_number
        self.reason = reason
        self.time = datetime.now()
        call.id += 1

    def display(self):
        print "=" * 20
        print self.unique_id
        print self.name
        print self.phone_number
        print self.reason
        print str(self.time)

class call_center(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)

    def add(self, add_call):
        self.calls.append(add_call)
    
    def remove(self, remove_call):
        self.calls.remove(remove_call)

    def info(self):
        for call in self.calls:
            call.display()

def takecall():
    name = raw_input("What is your name? ")
    phone_number = raw_input("Your phone number? ")
    reason = raw_input("What is your reason for calling?")
    return call(name, phone_number, reason)


center = call_center()
phone_tree = input("To make a call enter [1] for yes [0] for no: ")
if phone_tree == 1:
    center.calls.append(takecall())
    center.info()
else:
    phone_tree = False

