# Python solution
xs = [10, 15, 25, 35, 45]
for i, x in reversed(list(enumerate(xs))):
    print(i, x)

print("")
    
# unPythonic solution
for i in range(len(xs)- 1, -1, -1): #we iterate from last index to 0 (inclusive), so stop = -1
    print(i, xs[i])
