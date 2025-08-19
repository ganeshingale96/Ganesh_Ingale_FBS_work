# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

def armstrong_num(num):
    digit_count = count_digits(num)
    temp = num
    sum_of_powers = 0
    
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** digit_count
        temp = temp // 10
    
    return num == sum_of_powers

def check_armstrong(num):
    if armstrong_num(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

n = int(input("Enter the number: "))
check_armstrong(n)
