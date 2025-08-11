# 6. WAP to check if a given number is prime number or not.

num = int(input("Enter the number you want to check: "))
i = 2
while(i<num):
    if(num%i==0):
        print("Number is Not prime number.")
        break
    i+=1
else:
    print("Number is a prime number.")
    