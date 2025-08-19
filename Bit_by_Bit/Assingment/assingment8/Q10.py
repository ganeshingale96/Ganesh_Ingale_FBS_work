# 10. Write a program to check if entered year is a leap year or not.
def check_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(f'{year} is leap year')
            else:
                print(f'{year} is not leap year')
        else:
            print(f'{year} is leap year')
    else:
        print(f'{year} is not leap year')

y = int(input("Enter the year you want to check: "))    
check_leap_year(y)