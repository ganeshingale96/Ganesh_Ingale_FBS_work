# 8. Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)
import random
ran_num = random.randint(1111,9999)
uid = input("Enter the correct UID: ")
passw = int(input("Enter the correct Password: "))

if(uid=='Admin' and passw == 12345):
    print(f'CAPTCHA: {ran_num}')
    capt = int(input("Enter the captcha: "))

    if(ran_num==capt):
        print("Wellcome to site")
    else:
        print("Please Enter Valid captcha!!")      
else:
    print("Please Enter Valid UID & Password.")