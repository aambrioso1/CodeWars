"""
For the example given in the problem
a = 12
b = 20
c = 18
alpha = 45
beta = 30
gamma = 60
"""

from math import * # Needed for the trig functions, pi, and the trunc function.

# A helper function to convert decimal part degrees to minutes or for minutes to seconds
def convert(value):
	return (value - trunc(value)) * 60

def solve(a, b, c, alpha, beta, gamma):
	RAD = pi / 180
	alpha = alpha * RAD
	beta = beta * RAD
	gamma = gamma * RAD

	x = a * cos(alpha) - b * sin(beta) - c * cos(gamma)
	y = a * sin(alpha) + b * cos(beta) - c * sin(gamma)
	distance = sqrt(x ** 2 + y ** 2)
	angle = (pi + atan(y/x)) / RAD
	minutes = convert(angle)
	seconds = convert(minutes)

	return [round(distance,0), trunc(angle), trunc(minutes), trunc(seconds)]

print("distance and angle")
print(f'{solve(a, b, c, alpha, beta, gamma)}')
