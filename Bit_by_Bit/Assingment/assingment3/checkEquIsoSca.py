# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

ang1 = int(input("Enter the angle one: "))
ang2 = int(input("Enter the angle secound: "))
ang3 = int(input("Enter the angle third: "))


if(ang1==ang2==ang3):
    print("triangle is equilateral")
elif(ang1==ang2 or ang2==ang3 or ang1==ang3):
    print("triangle is isosceles")
else:
    print(" triangle is scalene")


