# 8. Write a program to convert days into years, weeks and days.

days = int(input("Enter number of days: "))

years = days // 365

rem_days = days % 365

weeks = rem_days // 7
rem_days = rem_days % 7

print(f'{years}-years,{weeks}-weeks,{rem_days}-remaining days.')