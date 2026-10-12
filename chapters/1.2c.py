import math

def square(x):
    return x ** 2

names = {square : "square", math.sqrt : "sqrt", math.exp : "exp"}

def descr(f, x):
    print(names[f], x, f(x))
    
descr(square, 4)
descr(math.sqrt, 16)