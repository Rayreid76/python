import random
random_num = random.randint(60,100)

print(random_num)

if (random_num >= 90):
    print("Score: ",random_num,"; your grade is an A.")
elif(80 <= random_num < 90):
    print("Score: ",random_num,"; your grade is an B.")
elif(70 <= random_num < 80):
    print("Score: ",random_num,"; your grade is an C.")
else:
    print("Score: ",random_num,"; your grade is an D.")