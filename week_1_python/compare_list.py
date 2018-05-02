#b = [1,2,3,6,]

#a = [1,2,5,6,2]
#b = [1,2,5,6,2]

#b = [1,2,5,6,5,3]

#b = [1,2,5,6,5]

a = ['celery','carrots','bread','milk']
b= ['celery','carrots','bread','cream']


while list(a):
    if len(a) == len(b):
        if sum(a) == sum(b):
            print("list is the same")
            break
        else:
            print("list is not the same")
            break
    else:
        print("list not the same")
        break
