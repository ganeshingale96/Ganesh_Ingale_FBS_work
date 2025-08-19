# 1. Write a program to calculate area of rectangle

def areaOfRect(l,b):
    area = l*b
    return area

length = int(input("Enter the length of rectangle: "))
breadth = int(input("Enter the breadth of rectangle: "))
res = areaOfRect(length,breadth)

print(f'The area of rectangle: {res}')