# 1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

sub1 = int(input("Enter marks of maths subject: "))

sub2 = int(input("Enter marks of english subject: "))

sub3 = int(input("Enter marks of FDS subject: "))

sub4 = int(input("Enter marks of DB subject: "))

sub5 = int(input("Enter marks of CN subject: "))


gain_marks = sub1 + sub2 + sub3 + sub4 + sub5

total_marks = (gain_marks / 500) * 100


print(f'Total marks of percentage {total_marks} %.')
