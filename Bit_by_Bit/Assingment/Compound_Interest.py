# 5. Write a program to enter P, T, R and calculate Compound Interest.
P = float(input("Enter Principal amount: "))
T = float(input("Enter Time in years: "))
R = float(input("Enter Rate of interest: "))

compound_interest = P * ((1 + (R / 100)) ** T) - P

print(f'Compound Interest is {compound_interest}.')