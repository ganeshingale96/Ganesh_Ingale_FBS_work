# 4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

sid1 = int(input("Enter the side one: "))
sid2 = int(input("Enter the side secound: "))
sid3 = int(input("Enter the side third: "))

 
 

if(sid1+sid2 > sid3 and sid2+sid3>sid1 and sid1+sid3>sid2):
    print("triangle is valid")

else:
    print("triangle is not valid")
