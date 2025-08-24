# 5. Write a program to find factorial using recursion.
def facto(num):
    if num==0:
        return 1
    else:
        return num * facto(num-1)
n = int(input("Enter the number: "))
res = facto(n)
print(f'the factorial of {n}!: {res}')









