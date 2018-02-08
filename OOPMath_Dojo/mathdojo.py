# Assignment: MathDojo

# HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.
# PART I

# Create a Python class called MathDojo that has the methods add and subtract. 
# Have these 2 functions take at least 1 parameter.

# Then create a new instance called md. 
# It should be able to do the following task:
# md.add(2).add(2,5).subtract(3,2).result
# which should perform 0+2+(2+5)-(3+2) and return 4.

# PART II
# Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter 
# with any number of values passed into the list. 
# It should now be able to perform the following tasks:
# md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
# should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.

# PART III
# Make any needed changes in MathDojo in order to support tuples of values
#  in addition to lists and singletons. 

# Placing an asterisk before the name of a the parameter after the "normal'' parameters
# Allows us to pass in a variable number of arguments
#   or capture multiple arguments into a single parameter 
# Example:
# def varargs(arg1, *args):
#   print "Got "+arg1+" and "+ ", ".join(args)
# varargs("one") # output: "Got one and "
# varargs("one", "two") # output: "Got one and two"
# varargs("one", "two", "three") # output: "Got one and two, three"

# Create a Python class called MathDojo that has the methods add and subtract. 
# Have these 2 functions take at least 1 parameter.

# Then create a new instance called md. 
# It should be able to do the following task:
# md.add(2).add(2,5).subtract(3,2).result
# which should perform 0+2+(2+5)-(3+2) and return 4.

class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self,x,*y):
        self.yaddTotal = 0
        print "x is" + str(x)
        print "y is" + str(y)
        for i in range(0,len(y)):
            self.yaddTotal += y[i]
        self.result += x + self.yaddTotal
        print "finished add.  result is " + str(self.result)
        return self 
    def subtract(self,x,*y):
        print "in subract, result starts as " + str(self.result)
        self.ysubtractTotal = 0
        self.subtractResult = 0
        print "x is" + str(x)
        print "y is" + str(y)
        for i in range(0,len(y)):
            self.ysubtractTotal += y[i]
        print "subtractTotal " + str(self.ysubtractTotal)
        self.result -= x + self.ysubtractTotal
        return self
md = MathDojo()
#md.add(3,1)
#md.subtract(2)
# md.add(2)
# print md.subtract(5,2).result
# md.subtract(5,2)
# md.add(2).add(2,5).subtract(3,2)
# print md.add(2).add(2,5).result
print md.add(2).add(2,5).subtract(3,2).result
#md.result
