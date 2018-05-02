sl = ['magical','unicorns']
il = [2,3,1,7,4,12]
ml = ['magical unicorns',19,'hello',98.98,'world']

print(ml)
print(il)
print(sl)

def type_list(list):
    nl = ''
    amount = 0

    for value in list:
        if isinstance(value, int):
            amount += value
        elif isinstance(value, float):
            amount += value
        elif isinstance(value, str):
            nl += value

    if nl and amount:
        print ("The array you entered is of mixed type","\n",nl, "\n",amount)

    elif nl:
        print ("The array you entered is of string type","\n",nl)

    else:
        print ("The array you entered is of number(float or int) type","\n",amount)

print(type_list(ml))
print(type_list(il))
print(type_list(sl))