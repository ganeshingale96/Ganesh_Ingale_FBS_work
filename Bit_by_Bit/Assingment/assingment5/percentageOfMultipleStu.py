# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.
num_student = int(input("Enter the number of students: "))
std_perc = 0
for i in range(1,num_student+1):
        print(f'student{i}')
        sub1 = int(input("Enter marks of maths subject: "))
        sub2 = int(input("Enter marks of english subject: "))
        sub3 = int(input("Enter marks of FDS subject: "))
        sub4 = int(input("Enter marks of DB subject: "))
        sub5 = int(input("Enter marks of CN subject: "))
        gain_marks = sub1 + sub2 + sub3 + sub4 + sub5
        total_perc = (gain_marks / 500) * 100
        std_perc+=total_perc
     
        print(f'The percentage of student{i}: {total_perc}')
print("average percentage of students",std_perc/num_student)

