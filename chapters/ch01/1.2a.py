#1.2(a)
import math
def descr(f, x):
    print(f, x, f(x))
    
def square(x):
    return x ** 2

descr(square, 3)
descr(math.sqrt, 4)
descr(math.exp, 1)


