import collections
import itertools

def prime_factors(number):
    i = 2
    while i*i <= number:
        if number%i == 0:
            number /= i
            yield i
        else:
            i += 1
    if number>1:
        yield number

def product(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result

def get_divisors(number):
    pf = list(prime_factors(number))

    pf_mult = collections.Counter(pf)

    powers = [
        [factor ** i for i in range(count+1)]
        for factor, count in pf_mult.items()
    ]

    for prime_combo in itertools.product(*powers):
        yield product(prime_combo)


triangle_factor = []
number = 1
triangle_number = 1

while len(triangle_factor)<500:
    number += 1
    triangle_number += number
    triangle_factor = list(get_divisors(triangle_number))

print(triangle_number)
