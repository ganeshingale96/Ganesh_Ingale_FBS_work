# 6. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic
basic_sal = int(input("Enter the Basic salary: "))

daPer = int(input("Enter the percentage on DA: "))
taPer = int(input("Enter the percentage on TA: "))
hraPer = int(input("Enter the percentage on HRA: "))

da = (basic_sal*daPer)/100
ta = (basic_sal*taPer)/100
hra = (basic_sal*hraPer)/100

total_salary = basic_sal + da + ta + hra

print(f'Basic Salary:{basic_sal} \nDA:{da} \nTA:{ta} \nHRA:{hra} \nTotal:{total_salary}')