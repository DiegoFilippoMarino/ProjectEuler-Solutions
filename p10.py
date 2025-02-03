import math

prime = [2]

def is_prime(number, primes):
    limit = math.isqrt(number)
    for n in primes:
        if n > limit:
            break
        if number % n == 0:
            return False
    return True

for num in range(3,2_000_001,2):
    if is_prime(num, prime):
        prime.append(num)

print(sum(prime))