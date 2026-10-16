from math import sqrt

# physical constants and variables
hbar = 1.054e-34 # reduced Planck constant, J*S
m = 9.11e-31 # electron mass, kg
V = float(input('Enter the potential energy in eV: '))
E = float(input('Enter the kinetic energy in eV: '))

if E <= V:
    print('The formulas do not apply (total reflection R = 1)')
else:
    # wavevectors of both sides
    k1 = sqrt(2 * m * E) / hbar
    k2 = sqrt(2 * m * (E - V)) / hbar

    T = 4 * k1 * k2 / (k1 + k2) ** 2
    R = ((k1 - k2) / (k1 + k2)) ** 2

    print('Transmission probability is: ', T)
    print('Reflection probability is: ', R)
    print('Check', R + T)

