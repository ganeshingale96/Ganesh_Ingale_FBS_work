emp = int(input("Enter the number of emp: "))
total_salary = 0

for i in range(1, emp + 1):
    basic_salary = int(input(f"Enter the basic salary for employee {i}: "))
    if basic_salary < 20000:
        da = (basic_salary * 10) / 100
        ta = (basic_salary * 12) / 100
        hra = (basic_salary * 15) / 100
        each_per_salary = basic_salary + da + ta + hra
        print(f'Salary of employee {i}: {each_per_salary}')
    else:
        da = (basic_salary * 15) / 100
        ta = (basic_salary * 18) / 100
        hra = (basic_salary * 20) / 100
        each_per_salary = basic_salary + da + ta + hra
        print(f'Salary of employee {i}: {each_per_salary}')
    total_salary += each_per_salary
print(f'Total salary of all employees: {total_salary}')
