'''Create a generator (stored in the variable practice_generator) that is capable of returning 
multiples of 7 indefinitely, starting from 7 itself, and that each time it is called returns the 
next multiple (7, 14, 21, 28... ).'''


def always_go():
    num = 0
    while True:
        yield num
        num += 7
        

practice_generator = always_go()

print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))


