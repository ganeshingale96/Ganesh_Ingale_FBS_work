# 4. WAP to print factorial of a number .
num = int(input("Enter the number you want factoral: "))
fact = 1
i = 1
while(i<=num):
    fact *= i
    i+=1
print(f'factorial of a number {num}!: {fact}')