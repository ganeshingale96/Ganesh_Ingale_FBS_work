# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+….. + n
# b. 1!+ 2! + 3! + 4!+….. + n!
# c. 1^1 + 2^2 + 3^3+ …… n^n

def n_num_ddition(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum
    
def fact_sum(n):
    sum = 0
    for i in range(1,n+1):
        fact = 1
        for j in range(1,i+1):
            fact*=j
        sum+=fact
    return sum

def n_power_n(n):
    sum = 0
    cal = 0
    for i in range(1,n+1):
        cal = i**i
        sum+=cal

    return sum

num = int(input("Enter the number: "))
qNum = input("a)1+ 2 + 3 + 4+….. + n\nb)1!+ 2! + 3! + 4!+….. + n!\nc)1^1 + 2^2 + 3^3+ …… n^n\nEnter the question number (a, b, or c): ")

if(qNum=='a'):
    result = n_num_ddition(num)
    print(f"Result Of N number addition : {result}")
elif(qNum=='b'):
    result = fact_sum(num)
    print(f"Result Of N number factorial addition : {result}")
elif(qNum=='c'):
    result = n_power_n(num)
    print(f"Result Of N number of N^N : {result}")
else:
    print("Invalid question number. Please enter a, b, or c.")  
