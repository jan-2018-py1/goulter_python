# Assignment: Product

# The owner of a store wants a program to track products. Create a product class to fill the following requirements.
# Product Class:
# Attributes:
#  Price
#  Item Name
#  Weight
#  Brand
#  Status: default "for sale"

# Methods:
#  Sell: changes status to "sold"
#  Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
#  Return: takes reason for return as a parameter and changes status accordingly. 
#    If the item is being returned because it is defective, change status to "defective" and change price to 0. 
#    If it is being returned in the box, like new, mark it "for sale". 
#    If the box has been, opened, set the status to "used" and apply a 20% discount.
#  Display Info: show all product details.

# Every method that doesn't have to return something should return self so methods can be chained.

class product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        #self.display_info()

    def sell(self):
        self.status = "sold"    
        return self
    def add_tax(self,myTax):
        tax = myTax
        self.price = self.price + (self.price * tax)
        return self
    def product_return(self, myReason):
        reason = myReason
        if reason == 'defective':
            self.status = reason
            self.price = 0
        elif reason == 'in box like new':
            self.status = 'for sale'
        elif reason == 'opened':
            self.status = 'used'
            self.price = self.price - (self.price * .2)

    def display_info(self):
        print "Price: " + str(self.price)
        print "Item Name: " + self.item_name
        print "weight: " + self.weight
        print "brand: " + self.brand
        print "status: " + self.status
        print "-------------------------------------"
        return self

prod1 = product(100, 'phone', '2oz', 'samsung')

prod1.sell()
prod1.add_tax(.1)
#prod1.product_return('defective')
#prod1.product_return('in box like new')
#prod1.product_return('opened')

prod1.display_info()







