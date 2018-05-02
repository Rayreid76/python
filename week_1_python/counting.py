#Multiples
#Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
for n in range(0, 1001):
    if(n%2):
        print(n)
#Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
#Sum List
for m in range(0, 100001):
    if(m%5):
        continue
    else:
        print(m)
#Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
s= 0
for a in [1, 2, 5, 10, 255, 3]:
    s += a
print ("total",s)
#Average List
#Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
print("Average ",s/6)
