import random

def mega():
    x = sorted(list(random.sample(range(1,61),6)))
    print(x)
    return x

def facil():
    x = sorted(list(random.sample(range(1,26),15)))
    print(x)
    return x

def luckday():
    x = sorted(list(random.sample(range(1,37),7)))
    month = random.choice(["jan", 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'out', 'nov', 'dec'])
    print(x, month)
    return x, month

while True:
    answer = int(input("Put 1 for megasena, 2 for lotofacil, 3 for luckday and 4 for close: "))
    match answer:
        case 1:
            mega()
        case 2:
            facil()
        case 3:
            luckday()
        case 4:
            break


