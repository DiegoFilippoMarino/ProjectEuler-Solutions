found = False

num = 1

while not found:
    for n in range(1,21):
        if num % n != 0:
            break
    else:
        found = True
        break
    num += 1

print(num)
