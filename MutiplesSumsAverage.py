# #Multiples
# 1) Part I - Write code that prints all the odd numbers from 1 to 1000. 
# Use the for loop and don't use a list to do this exercise.

# 2) Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

# 3) Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

# 4) Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

#1
print ("odds")
for i in range(1,10):
    if i%2!=0:
        print i

#2
print ("5s")
for i in range (1,20):
    if i%5==0:
        print i

#3
print ("sum exercise")
total = 0
a = [1, 2, 5, 10, 255, 3]
for i in a:
    total+=i
print (total)
#or
print(sum(a))

#4
print ("average exercise")
avg = 0.0
total = 0
a = [1, 2, 5, 10, 255, 3]
length = len(a)
for i in a:
    total += i
avg = (total/(length-1))
print (avg)






