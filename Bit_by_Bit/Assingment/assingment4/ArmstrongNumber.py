# 12. WAP to print Armstrong number within a given range
num = int(input("Enter the number: "))

temp = num
i = 1

count = 0

while(temp>0):
    temp = temp//10
    count+=1

sum = 0
temp = num

while(temp>0):
        d = temp%10
        sum = sum+(d**count)
        temp = temp//10

if(num == sum):
    print("This is a Armstrong number")
else:
    print("this is not a Armstrong number")

