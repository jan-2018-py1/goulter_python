# Assignment: Call Center

# You're creating a program for a call center. 
# Every time a call comes in you need a way to track that call. 
# One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

# You will create two classes. One class should be Call, the other CallCenter.
# Call Class
#  Create your call class with an init method. Each instance of Call() should have:
# Attributes:
#  unique id
#  caller name
#  caller phone number
#  time of call
#  reason for call
# Methods:
#  display: that prints all Call attributes.

# CallCenter Class
#  Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:
# Attributes:
#  calls: should be a list of call objects
#  queue size: should be the length of the call list
# Methods:
#  add: adds a new call to the end of the call list
#  remove: removes the call from the beginning of the list (index 0).
#  info: prints the name and phone number for each call in the queue as well as the length of the queue.
# You should be able to test your code to prove that it works. Remember to build one piece at a time and test as you go for easier debugging!
# Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.
# Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls get out of order? Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.
from datetime import datetime

class Call(object):
    def __init__(self, id, name, phone, time, reason):
        self.id = id
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason
    def display(self): #prints all Call attributes.
        print 'id: ' + str(self.id) + ' name: ' + self.name + ' phone: ' + self.phone + ' time: ' + self.time + ' reason: ' + self.reason
        return self


class Callcenter(object):
    def __init__(self): #still needs its own init
        self.calls = [] #list of call objects
        self.queuesize = 0 #length of the call list
    def add(self,Call): #adds a new call to the end of the call list
        self.calls.append(Call)
        self.queuesize += 1
        return self
    def remove(self): #removes the call from the beginning of the list (index 0).
        self.calls.pop(0)
        self.queuesize -= 1
        return self
    def info(self): #prints the name and phone number for each call in the queue as well as the length of the queue
        print self.queuesize
        for i in range(0,self.queuesize):
             print self.calls[i].name + ' ' + self.calls[i].phone
        return self
    # Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.
    def removeByPhone(self, yournumber):
        for i in range(0,self.queuesize):
             if self.calls[i].phone == yournumber:
                 self.calls.pop(i)
                 self.queuesize -= 1
        return self    
    # Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls get out of order? 
    # Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.            
    
c1 = Call(1,'glen','(111) 111-1111', str(datetime.now()), 'acceptance of job offer')
c2 = Call(2,'arielle','(222) 111-1111', str(datetime.now()), 'chilling with cats')
c3 = Call(2,'max','(333) 111-1111', str(datetime.now()), 'i am max')
c4 = Call(2,'linus','(444) 111-1111', str(datetime.now()), 'i am linus')
c5 = Call(2,'lucy','(555) 111-1111', str(datetime.now()), 'i am lucy')


center = Callcenter()
center.add(c1)
center.add(c2)
center.add(c3)
center.add(c4)
center.add(c5)
center.info()

center.remove().info().removeByPhone('(555) 111-1111').info()






