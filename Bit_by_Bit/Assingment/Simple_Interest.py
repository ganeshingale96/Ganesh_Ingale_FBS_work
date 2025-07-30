# 4. Write a program to enter P, T, R and calculate simple Interest.
P = float(input("Enter Principal amount: "))
T = float(input("Enter Time in years: "))
R = float(input("Enter Rate of interest: "))

simple_interest = (P * T * R) / 100

print(f'Simple Interest is {simple_interest}.')