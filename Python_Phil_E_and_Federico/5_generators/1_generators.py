'''Create a generator (stored in the practice_generator variable) that is capable of returning an 
infinite sequence of numbers, starting from 1, and returning a higher consecutive number each time 
it is called using next.'''

def infinite_sequence():
    num = 0
    while True:
        num += 1
        yield num

practice_generation = infinite_sequence()

print(practice_generation.next)
