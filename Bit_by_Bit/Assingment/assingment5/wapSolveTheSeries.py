# 8. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + …..n!

num = int(input("Enter the number: "))

sum = 0
for j in range(1, num+1):
    facto = 1
    for i in range(1, j+1):
        facto *= i 
    sum += facto
print(f'1! + …..{num}!:{sum}')

# b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)

n = int(input("Enter the number: "))
exp_sum = 0

for i in range(1,n+1):
    exp_sum += n**i
    
print(f'{n}^1 +…..+{n}^{n}: {exp_sum}')

# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input("Enter the number: "))
a = 1
total_sum = 0
for i in range(n):
    total_sum += a
    a *= 2
print(f'Sum of geometric series from 1 to {n} with common ratio 2: {total_sum}')

# d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10
a = int(input("Enter the value of a: "))
total_s = 0
for i in range(1,11):
    s = a * i / i  
    total_s += s
print(f'{a}/1 + {a}*2/2 + {a}*3/3 + ... + {a}*10/10: {total_s}')

# e. x - x^2/3 + x^3/5 - x^4/7 + …. to n terms
x = int(input("Enter the value of x: "))
n_terms = int(input("Enter the number of terms: "))
series_sum = 0
sign = 1
numerator = x 
for i in range(1, n_terms + 1):
    denominator = 2 * i - 1
    series_sum += sign * (numerator / denominator)
    sign *= -1
    numerator *= x  
print(f'Sum of the series x - x^2/3 + x^3/5 - ... to {n_terms} terms: {series_sum}')

