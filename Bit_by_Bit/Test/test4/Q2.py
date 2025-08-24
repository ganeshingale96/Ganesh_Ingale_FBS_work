# 2. Write a program to find factorial of given number using recursion
def fact_recur(num):
    if (num==0):
        return 1
    else:
        return num*fact_recur(num-1)
    
n = int(input("Enter the number: "))
res = fact_recur(n)
print(res)
