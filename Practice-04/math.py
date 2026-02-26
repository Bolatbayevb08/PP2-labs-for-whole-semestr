import math
import random

# 1. Degree to radian
degree = 15
radian = math.radians(degree)
print("Radian:", round(radian, 6))


# 2. Area of trapezoid
height = 5
base1 = 5
base2 = 6
area_trapezoid = ((base1 + base2) * height) / 2
print("Area of trapezoid:", area_trapezoid)


# 3. Area of regular polygon
n = 4
side = 25
area_polygon = (n * side ** 2) / (4 * math.tan(math.pi / n))
print("Area of polygon:", area_polygon)


# 4. Area of parallelogram
base = 5
height = 6
area_parallelogram = base * height
print("Area of parallelogram:", area_parallelogram)