# 6. Write a program to print Fibonacci series using recursion.
def fibo(num,a,b):
    if num==0:
        return 0
    else:
        c=a+b
        print(c)
        fibo(num-1,b,c) 
n = int(input("Enter the number: "))
a=-1
b=1
fibo(n,a,b)




