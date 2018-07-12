import random
my_list = []

def ran_list():
    for i in range(10):
        my_list.append(random.randint(0,100))

ran_list()
print "Random list: ", my_list

def sort(array):
    for i in range(len(array)):
        low_num = min(array[i:])
        min_index = array[i:].index(low_num)
        array[i + min_index] = array[i]
        array[i] = low_num

sort(my_list)
print "Sorted List: ",my_list