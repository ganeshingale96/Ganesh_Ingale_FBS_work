# 1. Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method

class Student:
    def __init__(self,sid=0,sn=0,sa=0,sp=0):
        self.sid = sid
        self.sname = sn
        self.sage = sa
        self.sper = sp
        
    def display(self):
        print("Student Id:-",self.sid)
        print("Student Name:-",self.sname)
        print("Student Age:-",self.sage)
        print("Student Percentage:-",self.sper)

    def accept(self):
        self.sid = int(input("Enter the Student ID: "))
        self.sname = input("Enter the Student Name: ")
        self.sage = int(input("Enter the Student Age: "))
        self.sper = float(input("Enter the Student Percentage: "))

    def calculate_rank(self):
        perc = self.sper
        if(perc >= 90):
            print('you passed with 1st rank')
        elif(perc >=80 and perc<90):
            print('you passed with second rank')
        elif(perc >=70 and perc<80):
         print('you passed with third rank')
        elif(perc >=60 and perc<70):
            print('you passed with fourth rank') 
        elif(perc >=50 and perc<60):
            print('you passed with fifth rank')
        else:
            print('you passed with ATKT')
    def __str__(self):
        return f'hello'

        
obj1 = Student()
# obj1.accept()
# obj1.display()
# obj1.calculate_rank()
print(obj1)
