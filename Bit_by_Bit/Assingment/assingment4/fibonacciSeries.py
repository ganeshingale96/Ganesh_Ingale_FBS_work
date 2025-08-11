# 5. WAP to print Fibonacci series upto n.
num = int(input("Enter the number you want Fibonacci series upto: "))
i = 0
a = -1
b = 1
c = 0

while(i<num):
    c =a+b
    print(c,end=' ')
    a = b
    b = c
    i+=1
