a, b, c = 0, 0, 0

for m in range(2,1000):
    for n in range(1,m):
        a = 2*m*n
        b = m**2-n**2
        c = m**2+n**2

        if a+b+c == 1000:
            print(a*b*c)
            break
    if a+b+c == 1000:
        break