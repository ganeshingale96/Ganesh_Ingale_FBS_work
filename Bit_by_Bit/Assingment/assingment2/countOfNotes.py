# 11. Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.
a = int(input("Enter the amount: "))
temp = a
c1 = temp//2000
temp = temp%2000

c2 = temp//500
temp = temp%500

c3 = temp//200
temp = temp%200

c4 = temp//100
temp = temp%100

c5 = temp//50
temp = temp%50

c6 = temp//20
temp = temp%20

c7 = temp//10
temp = temp%10

total_notes = c1+c2+c3+c4+c5+c6+c7
print(f'minimum number of notes needed for representing that ({a}) amount:{total_notes} 2k:{c1}notes 500:{c2}notes 200:{c3}notes 100:{c4}notes 50:{c5}notes 20:{c6}notes 10:{c7}notes')

