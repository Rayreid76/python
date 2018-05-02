""" input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']
def find_character(word_list, char):
    new_list = []
    for i in range(0, len(word_list)):

        if word_list[i].find(char) != -1:
            new_list.append(word_list[i])

    print new_list

test_list = ['hello','world','my','name','is','Anna']
find_character(test_list, 'o')"""

def findChar(alist, b):
    a = []
    i = 0
    while i < len(alist):
        if alist[i].find(b) !=-1:
            a.append(alist[i])
        i += 1

    print(a)

word_list = ['hello','world','my','name','is','Anna']
findChar(word_list,'a')

