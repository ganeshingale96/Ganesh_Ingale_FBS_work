# 10. Write a program to reverse three-digit number.

num = int(input("Enter the tree digit number: "))
temp = num

d1 = temp%10
temp = temp//10

d2 = temp%10
temp = temp//10


print(f'Reverse three-digit number is:{d1}{d2}{temp}')