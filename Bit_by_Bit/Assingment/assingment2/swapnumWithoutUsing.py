# Without using third variable------
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the secound number: "))

num1 = num1+num2
num2 = num1-num2
num1 = num1-num2

print(f'After swapping the first number:{num1} and secound number:{num2}')

# Using ',' method------------
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the secound number: "))
num1,num2 = num2,num1
print(f'After swapping the first number:{num1} and secound number:{num2}')