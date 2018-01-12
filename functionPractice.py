# Assignment: Fun with Functions
# Create a series of functions based on the below descriptions.

# 1) Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. 
# As your loop executes have your program print the number of that iteration and 
# specify whether it's an odd or even number.

# Your program output should look like below:
# Number is 1.  This is an odd number.
# Number is 2.  This is an even number.
# Number is 3.  This is an odd number.
# ...
# Number is 2000.  This is an even number.

# 2) Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16])
# and returns a list where each value has been multiplied by 5.
# The function should multiply each value in the list by the second argument. 
# For example, let's say: a = [2,4,10,16] Then: b = multiply(a, 5)
# print b
# Should print [10, 20, 50, 80 ].

# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. 
# Your new function should return the multiplied list as a two-dimensional list. 
# Each internal list should contain the 1's times the number in the original list. Here's an example:

# def layered_multiples(arr):
#   # your code here
#   return new_array
# x = layered_multiples(multiply([2,4,5],3))
# print x
# # output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

#1
def counter():
    for i in range(1,10):
        if i % 2 == 0:
            print i, "is even"
        else:
            print i, "is odd"

def multiply(mylist,number):
    b = []
    for i in mylist:
        b.append(i * number)
    return b

def my2dlist(mylist):
    #print mylist
    d=[]
    c=[]
    for i in mylist: #[6, 12, 15]
        for j in range (0,i):
            #print 1
            c.append(1)
        d.append(c)
        c=[]
    print d
 



a = [2,4,10,16]
num = 5
num2 = 3
#counter()
# c=multiply(a,num)
# print c
my2dlist(multiply([2,4,5],num2))
