# Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" 
# 1) print the position of the first instance of the word "day". 
# 2) create a new string where the word "day" is replaced with the word "month".

# Min and Max
# 3) Print the min and max values in a list like this one: 
# x = [2,54,-2,7,12,98]. Your code should work for any list.

# First and Last
# 4) Print the first and last values in a list like this one: 
# x = ["hello",2,54,-2,7,12,98,"world"]. 
# 5) Now create a new list containing only the first and last values in the original list. 
# Your code should work for any list.

# New List
# 5) Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. 
# Sort your list first. Then, split your list in half. 
# Push the list created from the first half 
# to position 0 of the list created from the second half. 
# The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. 
# Stick with it, this one is tough!

words = "It's thanksgiving day. It's my birthday,too!"

#1
print(words.find("day"))

#2
newWords=words.replace("day", "month")
print (newWords)

#3)
x = [2,54,-2,7,12,98]
print(min(x))

#4)
x = ["hello",2,54,-2,7,12,98,"world"]
length = len(x)
print x[0]
print x[length-1]
new = [x[0],x[length-1]]
print(new)

#5)
x = [19,2,54,-2,7,12,98,32,10,-3,6]
y = x.sort()
y = sorted(x)
print (y)
# lengthfloat = len(y)*1.0
# lengthcheck1 = len(y)*1.0 / 2
lengthcheck2 = len(y) / 2
# if lengthcheck1!=lengthcheck2:
#create a string with lengthcheck2 length and another string with lengthcheck2+1 length
string1 = x[:lengthcheck2]
string2 = x[lengthcheck2:]
print (string1)
print (string2)
string3 = [string1]+string2
print (string3)







