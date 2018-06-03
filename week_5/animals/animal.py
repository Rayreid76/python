class Animal(object):
    def __init__(self, name, health):
        self.name = name 
        self.health = health
        

    def Walk(self, id):
        for i in range(0, id):
            self.health = self.health - 1
        return self

    def Run(self, id):
        for i in range(0, id):
            self.health = self.health - 5
        return self

    def display(self):
        print "Animal: "+ self.name +", Health: "+ str(self.health)
        return self

class Dog(Animal):
    def __init__(self, name):
        self.health = 150
        self.name = name
    def Pet(self, id):
        for i in range(0, id):
            self.health = self.health + 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        self.name = name
        self.health = 170
    def Fly(self, id):
        for i in range(0, id):
            self.health = self.health - 10
        return self


animal1 = Animal('Zebra', 125)
animal2 = Dog('dog')
animal3 = Dragon('toddy')
animal1.Walk(3).Run(2).display()
animal2.Walk(3).Run(2).Pet(1).display()
animal3.Walk(3).Run(2).Fly(1).display()
#animal2.Walk(3).Run(2).Fly(1).display()





