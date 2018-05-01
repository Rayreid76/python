#Find and replace
words = "It's Thanksgiving day. It's my birthday, too!"
print(words)
print (words.find("day"))
words = words.replace("day","month")
print(words)

#Min an Max
x = [2,54,-2,7,12,98]
print(x)
print(min(x))
print(max(x))

#find and last
y = ["hello",2,54,-2,7,12,98,"world"]
print(y)
d = y[0] + y[7]
print(d)

#new list
t = [19,2,54,-2,7,12,98,32,10,-3]
print(t)
t.sort()
print(t)
f = t[0:5]
l = t[5:]
print(f)
print(l)
#l = t[len(t)/2:]
l.insert(0, f)
print(l)
