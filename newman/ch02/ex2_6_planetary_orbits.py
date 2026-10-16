from math import sqrt, pi

# Constants
G = 6.6738e-11      # gravitational constant, m^3 kg^-1 s^-2
M = 1.9891e30       # mass of the Sun, kg

# Input
l1 = float(input('Enter the perihelion distance in m: '))
v1 = float(input('Enter the perihelion velocity in m/s: '))

# Coefficients of v2^2 + B*v2 + C = 0
B = -2 * G * M / (v1 * l1)
C = -(v1**2 - 2 * G * M / l1)

# Smaller root (minus sign, since the leading coefficient is 1 > 0)
v2 = (-B - sqrt(B**2 - 4 * C)) / 2

# Orbit parameters
l2 = l1 * v1 / v2               # aphelion distance
a = (l1 + l2) / 2               # semi-major axis
b = sqrt(l1 * l2)               # semi-minor axis
T = 2 * pi * a * b / (l1 * v1)  # orbital period, s
e = (l2 - l1) / (l2 + l1)       # eccentricity

print('Aphelion distance l2 =', l2, 'm')
print('Aphelion velocity v2 =', v2, 'm/s')
print('Orbital period T =', T / (365.25 * 24 * 3600), 'years')
print('Eccentricity e =', e)