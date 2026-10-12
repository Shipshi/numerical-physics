import math

def fa(x):
    return math.sin(x)

def fb(x):
    return x ** 2

def der(f, x, h = 0.01):
    return (f(x + h) - f(x)) / h

def caller_b(a, b, x):
    return der(lambda t: a * fa(t) + b * fb(t), x)


def caller_d(a, b, x):
    def func(x):
        return (a * fa(x) + b * fb(x))
    return der(func,x)

def caller_e(a, b):
    def func(x):
        return a * fa(x) + b * fb(x)
    return func 

print(caller_b(2, 3, 1.0))
print("")
print(caller_d(2, 3, 1.0))
print("")
print(der(caller_e(2, 3), 1.0))