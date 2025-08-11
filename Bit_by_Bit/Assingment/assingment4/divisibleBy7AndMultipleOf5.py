# 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
a = int(input("Enter the starting number(from1): ")) 
b = int(input("Enter the ending number: "))


for i in range(a,b):
    if(i%7==0 and i%5==0):
        print(f'Numbers are divisible by 7 and multiple of 5 is: {i}')
