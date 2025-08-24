def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)

def sum_fact(n):
    if n == 1:
        return 1
    else:
        return fact(n) + sum_fact(n - 1)

n = int(input("Enter the number: "))
res = sum_fact(n)
print(res)

