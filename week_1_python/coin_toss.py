"""Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears. Hint: Use the python built-in round function to convert that floating point number into an integer.
x = .23945593
y = .798839238
x_rounded = round(x)
x_rounded will be rounded down to 0
y_rounded = round(y)
y_rounded will be rounded up to 1
"""
import random

t = []

def coin_toss(flip):
    for i in range(0, flip):
        chance = random.random()
        x = round(chance)
        t.append(x)
        total = sum(t)
    tails = flip - total
    print("There were",total,"heads and",tails,"tails out of", flip,"tosses.")
        


coin_toss(5000)
