numbers = list(range(1,101))

sum_squares = 0

for n in numbers:
    sum_squares += n**2

diff = sum(numbers)**2 - sum_squares

print(diff)