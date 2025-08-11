# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.
max_attempt = 3
user_id = 'Admin123'
password = 'Pass123'
for i in range(1,max_attempt+1):
    userid = input("Enter the user ID: ")
    passw = input("Enter the Password: ")

    if(userid==user_id and passw ==password):
        print("wellcome!")
        break
    else:
        if(i<max_attempt):
            print("Incorrect credentials. Try Again.")
        else:
            print("You have reached the maximum login limit!")

        
    