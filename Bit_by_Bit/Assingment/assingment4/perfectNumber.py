# 10. WAP to check if given number is Perfect Number.
num = int(input("Enter the number: "))
sum = 0
for i in range(1,num//2+1):
    if(num%i==0):
        sum+=i
if(num==sum):
    print("The given number is Perfect Number")
else:
    print("The given number is not Perfect Number")