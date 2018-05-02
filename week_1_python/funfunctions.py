def oddeven():
    i = 0
    while i<2001:
        if i%2:
            print("Number is ",i,". This number is odd.")
        else:
            print("Number is ",i,". This number is even.")
        i = i + 1
oddeven()

def mult():
    a = [2,4,6,10,16]
    b = 5
    c =[]
    for i in range(0, len(a)):
        c.append(a[i] * b)
        pass
    print(c)
mult()
