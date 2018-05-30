class product(object):
    def __init__(self, price, itemName, weight, brand):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
    def Sell(self):
        self.status = 'sold'
        print self.status
        return self
    
    def Return(self, id):
        if id == 1:
            self.status = 'defective'
            self.price = 0
            print self.status
        else:
            self.status = 'Used'
            self.price = self.price * .8 
            print self.status       
        return self
    
    def Addtax(self):
        self.total = self.price * 1.012
        print "Price + Tax: $" + str(self.total)
        return self
        

    def Display(self):
        print self.status 
        print "Price: $"+ str(self.price)
        print "Name: "+ self.itemName
        print "Weight: "+ str(self.weight) + " .oz"
        print "Brand: " + self.brand
        print "==========================="
        return self

        
product1 = product(1.99, 'Candy', .08, 'Mill')
product1.Display()
product1.Addtax().Return(2).Display()
product1.Addtax().Display()
product1.Addtax().Return(1).Display()
