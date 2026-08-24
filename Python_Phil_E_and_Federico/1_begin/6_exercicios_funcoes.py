'''Write a function called count_primes() that requires a single numeric argument.
This function must display on the screen how many prime numbers there are in the 
range from zero to that number included, and then return the number of prime numbers found.
Note: By convention 0 and 1 are not considered primes'''

def count_prime_numbers(number):

    prime_numbers = [2]
    iteration = 3

    if number < 2:
        return 0

    while iteration <= number:
        for n in range(3, iteration, 2):
            if iteration %n == 0:
                iteration += 2
                break
        else:
            prime_numbers.append(iteration)
            iteration += 2

    print(prime_numbers)
    return len(prime_numbers)


print(count_prime_numbers(1))