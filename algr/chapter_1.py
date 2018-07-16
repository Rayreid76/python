# setting and swapping
#myNumber = 42
#myName = "Ray"
#print myName, myNumber
#myName, myNumber = myNumber, myName

#print myName, myNumber

# pritn -52 to 1066
#many = []
#for i in range(-52,1067, 1):
#    many.append(i)
#print many

def beCheerful():
    gm = "Good Morning!"
    for i in range(98):
        print gm

#beCheerful()

def mulptile3():
    for i in range(-300, 1, 3):
        if i == -6 or i == -3:
            pass
        else:
            print i

#mulptile3()

def countdown(num):
    count = []
    for i in range(num, -1, -1):
        count.append(i)
    print count
#countdown(15)

arr = [1,3,5,7,9,13]
def greaterthan():
    for i in range(0,len(arr), 1):
        if arr[i] >= arr[1]:
            print arr[i]
#greaterthan()

def numbers(num1, num2):
    if num1 == num2:
        print "Jinxs"
    if num1 > num2:
        print num1, "is greater than", num2
    if num2 > num1:
        print num2, "is greater than", num1
#a = int(input("choose a number: "))
#b = int(input("choose a number: "))
#numbers(a,b)

def fartocel(num):
    celcius = (num-32)/1.8
    print celcius, "C"

def celtofar(num):
    fah = ((9.0/5.0)*num)+32
    print fah, "F"

c = float(input("Enter Fahrenheit: "))
d = float(input("Enter Celcius: "))
fartocel(c)
celtofar(d)