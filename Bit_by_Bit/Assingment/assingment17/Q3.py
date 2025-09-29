# 3. Create a class MedicalStudent inherited from Student with following
# :
# i. Data members :Specialization
# ii. MarksOfInternship
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method

class Student:
    def __init__(self,spe = 0):
        self.specialization = spe
        
    def display(self):
        print("Specialization:-",self.specialization)

class MedicalStudent(Student):
    def __init__(self,spe=0,moi=0):
        super().__init__(spe)
        self.moi=moi
    
    def display(self):
        super().display()
        print("MarksOfInternship:-",self.moi)
      
    def accept(self):
        self.specialization = input("Enter the Specialization: ")
        self.moi = float(input("Enter the MarksOfInternship : "))

    def calculate_rank(self):
        perc = self.moi
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


obj1 = MedicalStudent()
obj1.accept()
obj1.display()
obj1.calculate_rank()
