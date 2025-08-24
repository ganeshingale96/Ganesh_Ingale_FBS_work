# 9. Write a program to calculate the m to the power n using recursion.
def power(n,m = 1):
    if n == 0:
        return 0
    else:
        return m**n+power(n-1,m)

m = int(input("Enter the number: "))
n = int(input("Enter the number: "))
print(f'the m**n = {power(n,m)}')