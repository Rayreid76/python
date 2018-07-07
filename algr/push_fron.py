a = [1,12,123,34,53,64,23,75,3,345,99,43]

def push_front(arr, val):
    arr.reverse()
    arr.append(val)
    arr.reverse()
    print arr
    return
push_front([1,12,123,34,53], 52)