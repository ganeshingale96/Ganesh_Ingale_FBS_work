# Using three variable------------

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the secound number: "))

temp = num1
num1 = num2
num2 = temp

print(f'After swapping the first number:{num1} and secound number:{num2}')