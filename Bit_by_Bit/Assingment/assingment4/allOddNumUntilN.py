# 2. WAP to print all odd numbers until n.
n = int(input("Enter the number until which you want odd numbers: "))
i = 1
while(i<=n):
    if(i%2!=0):
        print(f'Odd number until {n}:{i}')
    i+=1
