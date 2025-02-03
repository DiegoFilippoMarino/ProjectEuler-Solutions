primes = set()

num_primes = 0

def is_prime(number, primes):
    if not primes:
        primes.add(number)
        return True

    for n in primes:
        if number % n == 0:
            return False
    else:
        return True

number = 2

while num_primes < 10001:
    if is_prime(number, primes):
        num_primes += 1
        primes.add(number)
    number += 1
print(number-1)