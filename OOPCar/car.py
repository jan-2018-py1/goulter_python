# Assignment: Car

#Create a class called  Car. 
# In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. 
# If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

#Create six different instances of the class Car. 
# In the class have a method called display_all() that returns all the information about the car as a string. 
# In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        #self.tax = self.taxPrice()
        self.tax = .12
        self.taxPrice()
        self.display_all()
        
    def taxPrice(self):
        if self.price > 10000:
            self.tax = .15
        return self
    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + self.speed
        print "Fuel: " + self.fuel
        print "Mileage: " + self.mileage
        print "Tax: " + str(self.tax)
        print "-------------------------------------"
        return self



car1 = car(1000, '10mph', 'extemely low', '15mpg')
car2 = car(100001111, '20mph', 'really low', '20mpg')
car3 = car(1, '30mph', 'low', '30mpg')
car4 = car(10000, '40mph', 'medium', '40mpg')
car5 = car(10005, '50mph', 'medium/high', '50mpg')
car6 = car(10000, '40mph', 'high', '60mpg')




