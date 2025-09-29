# 2. Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method
class Student:
    def __init__(self,Branch = 0):
        self.Branch = Branch
        
    def display(self):
        print("Branch:-",self.Branch)
     
class EnggStudent(Student):
    def __init__(self,Branch=0,im=0):
        super().__init__(Branch)
        self.im=im
    
    def display(self):
        super().display()
        print("Internal Marks:-",self.im)
      
    def accept(self):
        self.Branch = input("Enter the branch: ")
        self.im = float(input("Enter the Internal Marks : "))

    def calculate_rank(self):
        perc = self.im
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


obj1 = EnggStudent()
obj1.accept()
obj1.display()
obj1.calculate_rank()
