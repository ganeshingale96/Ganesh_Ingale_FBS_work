# 13. Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

unit = int(input("enter the electricity units : "))
cost = 110
if(unit>0):
    if(unit>50):
        if(unit>150):
            if(unit>250):
                cost = 50*0.50
                cost = 100*0.75
                cost = 100*1.20
                cost = cost+((unit-250)*1.50)
                cost = cost + (cost * 0.2)
                print(f'After the adding surcharge Total electricity bill is: {cost}')
                
            else:
                cost = 50*0.50
                cost = 100*0.75 
                cost = cost+((unit-150)*1.20) 
                cost = cost + (cost * 0.2)
                print(f'After the adding surcharge Total electricity bill is: {cost}')
                
        else:
            cost = 50*0.50
            cost = cost+((unit-50)*0.75)
            cost = cost + (cost * 0.2)
            print(f'After the adding surcharge Total electricity bill is: {cost}')
    else:
        cost = unit*0.50
        cost = cost + (cost * 0.2)
        print(f'After the adding surcharge Total electricity bill is: {cost}')
        
else:
    print("Please Enter Valid Units!!")






