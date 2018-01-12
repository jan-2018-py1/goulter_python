# Assignment: Find Characters
# Write a program that takes a list of strings and a string containing a single character, 
# and prints a new list of all the strings containing that character.

# Here's an example:

# # input
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# # output
# new_list = ['hello','world']
# Hint: how many loops will you need to complete this task?

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []

for word in word_list:
    # print word
    if word.count(char):
     #print word.count(char)
     #print word
     new_list.append(word)
print new_list