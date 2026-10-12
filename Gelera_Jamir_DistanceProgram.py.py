import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print(f"The distance between the two points is: {distance:.2f}")
# Reflection: Using a library is practical because it provides ready-made functions that make calculations easier and faster. The math library helped simplify the distance calculation by using sqrt() and pow() instead of writing the calculations from scratch.