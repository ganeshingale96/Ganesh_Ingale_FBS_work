
# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

total_amo_all = 0

num_passe = int(input("Enter the number of passengers: "))
ticket_amo = int(input("Enter the per person ticket amount: "))

for i in range(1,num_passe+1):
    print(f'Passenger {i}')

    age = int(input(f"Enter the age of {i} person: "))

    if age < 12:
        dis = ticket_amo *0.3
        total_amo = ticket_amo - dis
        total_amo_all+=total_amo
        print(f"Total amount for {i} person is: {total_amo}")
    elif age > 59:
        dis = ticket_amo *0.5
        total_amo = ticket_amo - dis
        total_amo_all+=total_amo
        print(f"Total amount for {i} person is: {total_amo}")
    elif age >= 12 and age <= 59:
        total_amo = ticket_amo
        total_amo_all+=total_amo
        print(f"Total amount for {i} person is: {total_amo}")
    
print(f"Total amount for all persons is: {total_amo_all}")
