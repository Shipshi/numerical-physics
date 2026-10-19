n = 0
C = 1

while C <= 1000000000:
    print(C)
    C = (4*n + 2) * C // (n + 2)
    n += 1