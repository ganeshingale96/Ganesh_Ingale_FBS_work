# 6. Write a program to find print the following Fibonacci series using
# functions:
#  1 1 2 3 5 8 n terms
def fibonacci_series(n):
    a = 1
    b = 0
    c = 0
    for i in range(1,n+1):
        c = a + b
        a = b
        b = c
        print(c,end=' ')

num = int(input("Enter the number: "))
fibonacci_series(num)