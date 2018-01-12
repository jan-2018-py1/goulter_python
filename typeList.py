# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, 
# based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. 
# If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. 
# At the end of your program print the string, the number and an analysis of what the list contains. 
# If it contains only one type, print that type, otherwise, print 'mixed'.

# Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

# #input
# l = ['magical unicorns',19,'hello',98.98,'world']
# #output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"
# # input
# l = [2,3,1,7,4,12]
# #output
# "The list you entered is of integer type"
# "Sum: 29"
# # input
# l = ['magical','unicorns']
# #output
# "The list you entered is of string type"
# "String: magical unicorns"

# If the item is a string, concatenate it onto a new string. 
newString =''
num = 0

numCount=0
l = ['magical unicorns',19,'hello',98.98,'world']
#l = ['magical','unicorns']
#l = [2,3,1,7,4,12]
for i in l:
    if isinstance(i,basestring):
        newString+=i+" "
    elif isinstance(i,(int, float, long, complex)):
        num+=i
        numCount+=1

# At the end of your program print the string, the number and an analysis of what the list contains. 
# If it contains only one type, print that type, otherwise, print 'mixed'.
if numCount > 1 and (len(newString) > 0):
    print "The list is of mixed type"
elif len(newString)>0 and numCount==0:
    print "The list is of string type"
else: 
    print "The list is of number type"
print newString
print num


