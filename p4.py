def is_palindrome(number):
    return str(number) == str(number)[::-1]

largest = 0

for i in range(100,1000):
    for j in range(100,1000):
        if is_palindrome(i*j):
            largest = i*j if i*j>largest else largest

print(largest)