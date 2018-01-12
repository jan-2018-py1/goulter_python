# # Write a program that, given some value, tests that value for its type. Here's what you should do for each type:

# 1) Integer
# If the integer is greater than or equal to 100, print "That's a big number!" 
# If the integer is less than 100, print "That's a small number"

# String
# If the string is greater than or equal to 50 characters print "Long sentence." 
# If the string is shorter than 50 characters print "Short sentence."

# List
# If the length of the list is greater than or equal to 10 print "Big list!" 
# If the list has fewer than 10 values print "Short list."

# Test your program using these examples:
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
arr = [sI,mI,bI,eI,spI,sS,mS,bS,eS,aL,mL,lL,eL,spL]
# Hint: You might want to read about the type and isinstance functions.
# https://docs.python.org/2/library/functions.html#type
# https://docs.python.org/2/library/functions.html#isinstance

# 1) Integer
# If the integer is greater than or equal to 100, print "That's a big number!" 
# If the integer is less than 100, print "That's a small number"

for index in arr:
    if isinstance(index,int):
        if index >=100:
            print index, 'is a big number'
        else:
            print index, "That's a small number"
    elif isinstance(index,basestring):
        if len(index) >= 50:
            print index, 'Long Sentence'
        else:
            print index, 'Short Sentence'
    elif isinstance(index,list):
        if len(index) >= 50:
            print index, 'Big List'
        else:
            print index, 'Short List'
# print (arr[index])
# print (isinstance(arr[0],int))
# print (isinstance(sS,basestring))
# print (isinstance(spL,list))


