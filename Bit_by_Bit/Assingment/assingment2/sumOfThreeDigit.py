# 7. Find the sum of three-digit number.
num = int(input("Enter the tree digit number: "))
temp = num

d1 = temp%10
temp = temp//10

d2 = temp%10
temp = temp//10

sum = d1+d2+temp
print(f'the sum of three digit number {num} is {d1}+{d2}+{temp}={sum}')
