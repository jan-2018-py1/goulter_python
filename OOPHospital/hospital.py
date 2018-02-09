# Assignment: Hospital

# You're going to build a hospital with patients in it!

# Before looking at the requirements below, think about the potential characteristics of each patient and hospital. How would you design each?
# Patient Class:
# Attributes:
#  Id: an id number
#  Name
#  Allergies
#  Bed number: should be none by default

# Hospital Class

# Attributes:
#  Patients: an empty array
#  Name: hospital name
#  Capacity: an integer indicating the maximum number of patients the hospital can hold.

# Methods:
#  Admit: add a patient to the list of patients.
#   Assign the patient a bed number. 
    #If the length of the list is >= the capacity do not admit the patient. 
    # Return a message either confirming that admission is complete or saying the hospital is full.
#  Discharge: look up and remove a patient from the list of patients. 
#   Change bed number for that patient back to none.


class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = 'none'

class Hospital(object):
    def __init__(self, name, capacity): 
        self.patients = [] #list of list of patient objects
        self.name = name
        self.capacity = capacity # max patient classes the patients array can hold
    def admit(self,Patient): #adds a patient to the list of patients
        if len(self.patients) < self.capacity:
            self.patients.append(Patient)
            Patient.bed_number = str(len(self.patients))
            print "Admission of  " + Patient.name + " is complete"
            return self
        else:
            print "OVER/AT CAP!! we have " + str(len(self.patients)) + " and capacity for only " + str(self.capacity)
            return self

    def info(self): #prints the name and phone number for each call in the queue as well as the length of the queue
         for i in range(0,len(self.patients)):
              print self.patients[i].name + ' ' + self.patients[i].allergies + self.patients[i].bed_number
         return self
    #  Discharge: look up and remove a patient from the list of patients. 
#   Change bed number for that patient back to none.            
    
    #def discharge(self, patient_id):
    def discharge(self, patient_obj):
        loopend = len(self.patients) 
        print "length of patients is " + str(len(self.patients))
        #print "patient id is " + str(patient_id)
        print "patient id is " + str(patient_obj.id)
        # print self.patients[0].id
        
        
        for i in range(0,loopend):
            if self.patients[i].id == (patient_obj.id):
                 self.patients.pop(i)
                 patient_obj.bed_number = 'none'   
                 return self
        

p1 = Patient(1,'glen','advil')
p2 = Patient(2,'arielle','botox')
p3 = Patient(3,'max','catnip')
p4 = Patient(4,'linus','boxes')

h1 = Hospital('Mercy Hospital', 3)
h1.admit(p1)
h1.admit(p2)
h1.admit(p3)
h1.admit(p4)
h1.info()

print "1st p1 bed num " + p1.bed_number
h1.discharge(p1).info()
print "2nd p1 bed num " + p1.bed_number
#h1.discharge(p1)











