import random

def mega():
    x = sorted(random.sample(range(1,61),6))
    print(x)
    return x

def facil():
    x = sorted(random.sample(range(1,26),15))
    print(x)
    return x

def luck_day():
    months = random.choice(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
    x = sorted(random.sample(range(1,37),7))
    print(months, x)
    return months, x

while True:
    choice = int(input('Put 1 to megasena, 2 to lotofacil, 3 to luckday and 4 to exit: '))
    match choice:
        case 1:
            mega()
        case 2:
            facil()
        case 3:
            luck_day()
        case 4:
            break








