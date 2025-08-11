# 11. WAP to check if given number Strong Number.
num = int(input("Enter the number you want to check: "))
temp = num
i = 1
sum = 0

while(temp>0):
    d = temp%10
    temp = temp//10

    j=1 
    fact = 1

    while(j<=d):
        fact = fact*j
        j+=1
    sum+=fact

if(num == sum):
    print("This is a strong number")
else:
    print("this is not a strong number")



    

