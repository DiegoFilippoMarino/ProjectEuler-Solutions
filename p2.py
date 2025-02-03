sum = 2

a = 1
b = 2
fib = 0

while fib < 4*(10**6):
    fib = a + b
    a, b = b, fib
    sum += fib if fib%2==0 else 0

print(sum)