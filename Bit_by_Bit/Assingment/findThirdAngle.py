# 6. Write a Program to input two angles from user and find third angle of the triangle.
angle1 = float(input("Enter first angle of triangle: "))
angle2 = float(input("Enter second angle of triangle: "))

angle = 180 - (angle1 + angle2)

print(f'Third angle of trangle is {angle} degrees')