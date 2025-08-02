# 7. Write a program to check if user has entered correct userid and password.
uid = input("Enter the correct UID: ")
passw = int(input("Enter the correct Password: "))

if(uid=='Admin' and passw == 12345):
    print("Wellcome to site")
else:
    print("Please Enter Valid UID & Password.")
