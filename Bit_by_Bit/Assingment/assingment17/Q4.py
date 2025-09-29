# 4. Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method

class College:
    def __init__(self,num_students=0):
        self.students = [None]*num_students
    
    def add_student(self,student_name):
        for i in range(len(self.students)):
            if self.students[i] is None:
                self.students[i] = student_name
                return f"Student '{student_name}' added"
        return "No space to add more students"


    def get_student(self, student_name):
        if student_name in self.students:
            index = self.students.index(student_name)
            return self.students[index]
        else:
            return f"Student '{student_name}' not found."

    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            return f"Student '{student_name}' removed"
        return f"Student '{student_name}' not found."

num_stud = int(input("Enter the Number of student wants to add College: "))
iit_salokhenagar = College(num_stud)
choice = 0
while choice!=4:
    choice = int(input("1.Add Students\n2.Remove Students\n3.Get Students\n4.Exit\nEnter the task number: "))

    if choice==1:
        std_name = input("Enter the student Name you want to add: ")
        print(iit_salokhenagar.add_student(std_name))
    elif choice==2:
        std_name = input("Enter the student Name you want to remove: ")
        print(iit_salokhenagar.remove_student(std_name))
    elif choice==3:
        std_name = input("Enter the student Name you want to Get Details: ")
        print(iit_salokhenagar.get_student(std_name))
    elif choice==4:
        print("Thanks for choose us!")



