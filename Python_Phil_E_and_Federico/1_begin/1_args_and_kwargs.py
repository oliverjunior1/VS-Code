def return_distincts():
    dictionary = {}
    a = int(input("Put the value 1: "))
    dictionary['a'] = a

    b = int(input("Put the value 2: "))
    dictionary['b'] = b

    c = int(input("Put the value 3: "))
    dictionary['c'] = c
    
    total = sum([a, b, c])
    max_val = max(dictionary.values())
    min_val = min(dictionary.values())
    
    if total > 15:
        return max_val
    elif total < 10:
        return min_val
    else:
        return (-max_val - min_val) + total

print(return_distincts())
