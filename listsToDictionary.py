# Assignment: Making Dictionaries
# Create a function that takes in two lists and creates a single dictionary. 
# The first list contains keys and the second list contains the values. Assume the lists will be of equal length.

# Your first function will take in two lists containing some strings. Here are two example lists:

# name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
# favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
# Here's some help starting your function.

# def make_dict(list1, list2):
#   new_dict = {}
#   # your code here
#   return new_dict
# Hacker Challenge:
# If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.

name = ["Glen", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
favorite_animal2 = ["DOG", "horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    if len(list1) == len(list2):
        new_dict = zip(list1, list2) #only a list of tuples here
        theDictionary = dict(new_dict)
        return theDictionary
    else:
        new_dict = zip(list2, list1)
        theDictionary = dict(new_dict)
        return theDictionary

mydict =  make_dict(name,favorite_animal2)
print mydict



