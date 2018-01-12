# Assignment: Stars
# Write the following functions.
# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.
# For example:
# x = [4, 6, 1, 3, 5, 7, 25]
# draw_stars(x) should print the following when invoked:
# ****
# ******
# *
# ***
# *****
# *******
# *************************

# Part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. 
# When a string is passed, instead of displaying *, display the first letter of the string 
# according to the example below. 
# You may use the .lower() string method for this part.
# 
# For example:
# x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# draw_stars(x) should print the following in the terminal:
# ****
# ttt
# *
# mmmmmmm
# *****
# *******
# jjjjjjjjjjj


def draw_stars(mylist):
    for i in mylist:
        myString = ''
        #print '*' * i
        #or
        for j in range(0,i):
            myString+= '*'
        print myString

def draw_stars2(mylist):
    for i in mylist:
        if isinstance(i,(int, float, long, complex)):
            print '*' * i
        else:
             print i[0].lower() * len(i)
    

x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)
draw_stars2(y)