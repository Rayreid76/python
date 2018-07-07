import random
my_list = []

def ran_list():
    for i in range(25):
        my_list.append(random.randint(0,100))

ran_list()
print "Random list: ", my_list

def sort(list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(list)-1):
            if list[i] > list[i + 1]:
                sorted = False
                list[i], list[i + 1] = list[i + 1], list[i]

sort(my_list)
print "Sorted List: ",my_list