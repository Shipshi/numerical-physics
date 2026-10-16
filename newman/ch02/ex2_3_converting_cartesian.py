from math import atan

x = float(input('Enter x value:'))
y = float(input('Enter y value:'))

theta = atan(y / x)
r = (x ** 2 + y ** 2) ** 0.5

print('Polar radius is:', r)
print('Polar angle is:', theta)



