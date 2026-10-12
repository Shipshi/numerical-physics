# Python solution
xs = [10, 15, 25, 35, 45]
for i, x in reversed(list(enumerate(xs))):
    print(i, x)
    
    
# unPythonic solution
#xs = [10, 15, 25, 35, 45]
#for i in range(len(xs)- 1, -1, -1):
#    print(i, xs[i])