h = float(input("Enter the height of the tower in meters:"))
g = 9.81 # m/s^2

time = ((2 * h) / g) ** 0.5  # initial velocity is zero

print("Time to hit the ground:", time, "s")