'''Create a generator (stored in the practice_generator variable) that is capable of returning an 
infinite sequence of numbers, starting from 1, and returning a higher consecutive number each time 
it is called using next.'''

def generate_always():
    num = 0
    while True:
        yield num
        num += 1
        

x = generate_always()

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))