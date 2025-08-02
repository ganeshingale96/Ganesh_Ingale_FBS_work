# 13. Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

unit = int(input("enter the electricity unit charges: "))
if(unit<=50):
    cost = unit*0.50
elif(unit>50 and unit<=150):
    cost = unit*0.75
elif(unit>150 and unit<=250):
    cost = unit*1.20
elif(unit>250):
    cost = unit*1.50

print(f'The electricity bill is: {cost}')
cost = cost + (cost * 0.2)
print(f'After the adding surcharge Total electricity bill is: {cost}')


