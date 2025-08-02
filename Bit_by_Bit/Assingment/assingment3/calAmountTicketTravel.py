# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

age1 = int(input("Enter the age of first person: "))
age2 = int(input("Enter the age of second person: "))
age3 = int(input("Enter the age of third person: "))
age4 = int(input("Enter the age of fourth person: "))
age5 = int(input("Enter the age of fifth person: "))

ticket_amo = int(input("Enter the per person ticket amount: "))
total_amo = 0
# 1
if age1 < 12:
    dis = ticket_amo *0.3
    total_amo1 = ticket_amo - dis
    print(f"Total amount for first person is: {total_amo1}")
elif age1 > 59:
    dis = ticket_amo *0.5
    total_amo1 = ticket_amo - dis
    print(f"Total amount for first person is: {total_amo1}")
elif age1 >= 12 and age1 <= 59:
    total_amo1 = ticket_amo
    print(f"Total amount for first person is: {total_amo1}")
# 2
if age2 < 12:
    dis = ticket_amo *0.3
    total_amo2 = (ticket_amo - dis)
    print(f"Total amount for second person is: {total_amo2}")

elif age2 > 59:
    dis = ticket_amo *0.5
    total_amo2 = (ticket_amo - dis)
    print(f"Total amount for second person is: {total_amo2}")

elif age2 >= 12 and age1 <= 59:
    total_amo2 = (ticket_amo)
    print(f"Total amount for second person is: {total_amo2}")
# 3
if age3 < 12:
    dis = ticket_amo *0.3
    total_amo3 = (ticket_amo - dis)
    print(f"Total amount for third person is: {total_amo3}")
elif age3 > 59:
    dis = ticket_amo *0.5
    total_amo3 = (ticket_amo - dis)
    print(f"Total amount for third person is: {total_amo3}")
elif age3 >= 12 and age1 <= 59:
    total_amo3 = (ticket_amo)
    print(f"Total amount for third person is: {total_amo3}")
# 4
if age4 < 12:
    dis = ticket_amo *0.3
    total_amo4 = (ticket_amo - dis)
    print(f"Total amount for fourth person is: {total_amo4}")
elif age4 > 59:
    dis = ticket_amo *0.5
    total_amo4 =(ticket_amo - dis)
    print(f"Total amount for fourth person is: {total_amo4}")
elif age4 >= 12 and age1 <= 59:
    total_amo4 =(ticket_amo)
    print(f"Total amount for fourth person is: {total_amo4}")
# 5
if age5 < 12:
    dis = ticket_amo *0.3
    total_amo5 =(ticket_amo - dis)
    print(f"Total amount for fifth person is: {total_amo5}")
elif age5 > 59:
    dis = ticket_amo *0.5
    total_amo5 = (ticket_amo - dis)
    print(f"Total amount for fifth person is: {total_amo5}")
elif age5 >= 12 and age1 <= 59:
    total_amo5 = (ticket_amo)
    print(f"Total amount for fifth person is: {total_amo5}")


total_amount = total_amo1 + total_amo2 + total_amo3 + total_amo4 + total_amo5 
print(f"Total amount for all five people is: {total_amount}")
