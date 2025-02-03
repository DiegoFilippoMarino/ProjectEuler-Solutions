num = 600851475143

i = 2

while i*i <= num:
    if num % i != 0:
        i += 1
    else:
        num //= i #keeps removing the factors from num until only the largest prime remains

print(num)
