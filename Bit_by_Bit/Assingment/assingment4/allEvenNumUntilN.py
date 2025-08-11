# 1. WAP to print all even numbers until n.
n = int(input("Enter the number until which you want even numbers: "))
i = 1
while(i<=n):
    if(i%2==0):
        print(f'Even number until {n}:{i}')
    i+=1