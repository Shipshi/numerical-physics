from math import pi

#physical and mathematical constants
G = 6.67 * (10 ** (-11)) # Newton's Gravitational Constant, m^3 * kg^-1 * s^-2
M = 5.97 * (10 ** 24) # Mass of Earth in kg
R = 6371 * (10 ** 3) #Radius of earth in meters

#Physical variables
T = float(input("Enter the time in seconds:"))
T_1 = 86400 # 24 hours in seconds
T_2 = 5400 # 90 minutes in seconds
T_3 = 2700 # 45 minutes in seconds
T_sidereal = 86148 # 23.93 hours in seconds

h = (G * M * (T ** 2) / (4 * (pi ** 2))) ** (1 / 3) - R # altitude in meters
h_1 = (G * M * (T_1 ** 2) / (4 * (pi ** 2))) ** (1 / 3) - R
h_2 = (G * M * (T_2 ** 2) / (4 * (pi ** 2))) ** (1 / 3) - R
h_3 = (G * M * (T_3 ** 2) / (4 * (pi ** 2))) ** (1 / 3) - R
h_sidereal = (G * M * (T_sidereal ** 2) / (4 * (pi ** 2))) ** (1 / 3) - R 

dh = h_1- h_sidereal

print("The altitude is:", h, 'meters')
print("The altitude of satellites once a day:", h_1, 'meters')
print("The altitude of satellites once every 90 minutes:", h_2, 'meters')
print("The altitude of satellites once every 45 minutes:", h_3, 'meters')
print("The difference of altitudes of satelites between day and sidereal day:", dh, 'meters') 

# Answers
# (c)  Conclusion: a satellite with a 45-minute period is impossible, as it would have to move inside the Earth. This means that orbits around the Earth have a minimum period—approximately 84 minutes.
# (d) Because the earth is rotating not only on its own axis, but also around sun. A solar day (24 hours) is the time it takes for the Earth to complete one full rotation relative to the Sun. During this period, the Earth moves approximately 1 degree along its orbit. For the Sun to return to the same point in the sky, the Earth must rotate slightly more than 360 degrees, it changes around 82 km of height. A geosynchronous satellite must follow the Earth's rotation itself, i.e. one full
#360-degree turn, which takes a sidereal day, not a solar day.
