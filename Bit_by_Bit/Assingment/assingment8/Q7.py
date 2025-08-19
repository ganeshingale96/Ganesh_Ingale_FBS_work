# 7. Write a program to find sum of digits of a number.
def sum_of_digits(num):
    sum = 0
    temp = num
    for i in range(1,4):
        d = temp%10
        temp=temp//10
        sum+=d
    return sum

num = int(input("Enter the number: "))
result = sum_of_digits(num)
print(f'The sum of digits: {result}')




