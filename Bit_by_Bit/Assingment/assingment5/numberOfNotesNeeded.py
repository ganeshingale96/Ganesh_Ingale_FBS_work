# 5. Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount. (Use looping to optimize
# the problem)

amo = int(input("Enter the amount: "))

temp = amo
total_notes = 0

for i in (2000, 500, 200, 100, 50, 20, 10):
    count = temp // i
    temp = temp % i
    total_notes += count
    print(f'{i} notes required: {count}')
    
print(f'minimum number of notes needed for representing that ({amo}) amount:{total_notes}')
