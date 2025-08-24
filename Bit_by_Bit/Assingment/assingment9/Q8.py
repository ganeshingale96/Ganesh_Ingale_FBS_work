# 8. Write a program to check whether a number is prime or not using recursion.
def prime(num,i=2):
    if num==2:
        return True
    elif num % i== 0 or num<2:
        return False
    else:
        return True
      
    return prime(num,i+1)
num = int(input("Enter the number: "))

if prime(num):
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')