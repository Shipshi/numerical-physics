import math

def square(x):
    return x ** 2

funcs = {"square": square, "sqrt": math.sqrt, "exp": math.exp}

def descr(name, x):
    f = funcs[name]
    print(name, x, f(x))

descr("square", 4)
descr("exp", 1)
descr("sqrt", 16)