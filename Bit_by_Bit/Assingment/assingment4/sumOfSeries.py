# 3. WAP to print sum of series upto n.
num = int(input("Enter the number until which you want sum of series: "))
i = 0
sum = 0
while(i<=num):
    sum+=i
    i+=1
print(f'sum of series upto {num} is: {sum}')


