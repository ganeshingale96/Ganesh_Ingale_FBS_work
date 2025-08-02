# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

ang1 = int(input("Enter the angle one: "))
ang2 = int(input("Enter the angle secound: "))
ang3 = int(input("Enter the angle third: "))

sum = ang1+ang2+ang3

if(sum<=180):
    print("Entered triangle is valid")
else:
    print("Entered triangle is not valid")

