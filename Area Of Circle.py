# Area of circle using Monte Carlo Simulation
import math
import random


def areaOfCircle(points, radius=1):
    insideCircle = 0
    for i in range(points):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        if x**2 + y**2 <= radius**2:
            insideCircle += 1
    calculatedArea = 4 * radius ** 2 * insideCircle / points
    expectedArea = math.pi * radius ** 2
    print(f'Calculated Area: {calculatedArea}')
    print(f'Expected Area: {expectedArea}')
    print(f'Error: {abs(calculatedArea - expectedArea)}')


if __name__ == '__main__':
    points = 10000
    areaOfCircle(points)
