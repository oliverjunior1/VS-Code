import random

def mega():
    x = list(sorted(random.sample(range(1,61),6)))
    print(x)

def facil():
    x = list(sorted(random.sample(range(1,26),15)))
    print(x)

def luck_day():
    month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'out', 'nov', 'dec']
    choiced = random.choice(month)
    x = list(sorted(random.sample(range(1,35),7)))
    print(choiced, x)

while True:
    option = int(input("Put 1 to megasena, 2 to lotofacil, 3 to luckday or 4 to exit: "))
    match option:
        case 1:
            mega()
        case 2:
            facil()
        case 3:
            luck_day()
        case 4:
            break



