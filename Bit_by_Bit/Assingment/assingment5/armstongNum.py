# 4. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)
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
