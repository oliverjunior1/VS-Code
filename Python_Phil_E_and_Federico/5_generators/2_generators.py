'''Create a generator (stored in the practice_generator variable) that is capable of returning an 
infinite sequence of numbers, starting from 1, and returning a higher consecutive number each time 
it is called using next.'''

def infinity_generation():
    num = 0
    while True:
        yield num
        num += 1
        
        
        

x = infinity_generation()

print(next(x))
print(next(x))
print(next(x))
print(next(x))