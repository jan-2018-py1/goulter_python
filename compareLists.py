# Assignment: Compare Lists
# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

# Your program should be able to accept and compare two lists: list_one and list_two.
# If both lists are identicalc. 
# If they are not identical print "c." Try the following test cases for lists one and two:

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
#list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]
# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]
# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']

#compare type and length first
#then compare element by element

match = False
length1=len(list_one)
length2=len(list_two)
if length1 != length2:
    print 'different lengths'
else:
    for i in range(0,length1):
        if list_one[i] != list_two[i]:
            #print list_one[i], list_two[i], 'DONT match'
            match = False
            break
        else:
            #print list_one[i], list_two[i], 'match'
            match = True

if match == True: 
    print 'The lists are the same' 
else: 
    print 'The lists are NOT the same'

    

    
