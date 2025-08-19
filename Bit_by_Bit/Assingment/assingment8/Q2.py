# 2. Write a program to calculate area of circle

def areaOfCircle(r):
    area = 3.14*r**2
    return area

radius = int(input("Enter the radius of circle: "))
result = areaOfCircle(radius)
print(f'Area Of Circle Of {radius} radius is: {result}')

