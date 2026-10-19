from math import sqrt

L = 50
M = 0.0

for i in range(-L, L + 1):
    for j in range(-L, L + 1):
        for k in range(-L, L + 1):
            if i == 0 and j == 0 and k == 0:
                continue   #skip the atom
            if ( i + j + k) % 2 == 0:
                M += 1 / sqrt(i**2 + j**2 + k**2)  # Substituting the expression for V into M, we get:
            else:
                M -= 1 / sqrt(i**2 + j**2 + k**2) #if i + j + k is odd
print('Madelung constant equals to: ', M)