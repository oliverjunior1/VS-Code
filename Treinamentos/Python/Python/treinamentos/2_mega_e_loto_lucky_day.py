import random

def mega():
    x = sorted(random.sample(range(1,61),6))
    print(x)
    return x
    

def facil():
    x = sorted(random.sample(range(1,26),15))
    print(x)
    return x

def luck():
    month = random.choice(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
    x = sorted(random.sample(range(1,37),12))
    print(month, x)
    return month, x

while True:
    choice = int(input("Put 1 to megasena, 2 to lotofacil and 3 to luckday and 4 to exit: "))
    match choice:
        case 1:
            mega()
        case 2:
            facil()
        case 3:
            luck()
        case 4:
            break






