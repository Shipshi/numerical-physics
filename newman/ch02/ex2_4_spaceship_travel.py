# Physical variables and constants
x = float(input('Enter the distance in light years: '))
b = float(input('Enter the fraction of speed of light: '))

# input validation
if not (0 < b < 1):
    print('Speed must satisfy  0 < v/c < 1')
else:
    # (a)
    t = x / b #  time in the Earth system, years

    # (b) 
    tau = x * (1 - b ** 2) ** 0.5 / b # passenger's proper time, years

    print('Arrival time for an observer on Earth:', t, 'years')
    print('Arrival time for the spaceship passenger:', tau,'years')