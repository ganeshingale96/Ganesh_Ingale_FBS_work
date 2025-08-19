# 4. Sum of all odd numbers between 1 to n 
def sum_of_odd_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            sum+=i
    return sum

num = int(input("Enter the number: "))
result = sum_of_odd_numbers(num)
print(f'Sum of all odd numbers between 1 to {num}: {result}')