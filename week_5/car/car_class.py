"""Assignment: Car

Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined."""

class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = '15%'
        else:
            self.tax = '12%'

    def display_all(self):
        print "Price: $" + str(self.price)
        print "Speed: " + str(self.speed) + " mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage)
        print "Tax rate: " + str(self.tax)
        print "==================================="


car1 = car(10000, 85, 'full', 400000)
car2 = car(15000, 100, 'half full', 350000)
car3 = car(20000, 110, 'full', 200000)
car4 = car(30000, 115, 'empty', 185000)
car5 = car(45000, 136, 'half full', 75000)
car6 = car(55000, 196, 'half full', 35000)

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()


