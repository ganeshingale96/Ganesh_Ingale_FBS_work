# Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Complex_number:
    def __init__(self,real=0,imag=0 ):
        self.real = real
        self.imag = imag

    def __del__(self):
        print("Complete the task")
    
    def __add__(self,other):
        self.real = self.real + other.real
        self.imag = self.imag + other.imag
        return self

    def __add__(self,other):
        self.real = self.real + other.real
        self.imag = self.imag + other.imag
        return self
    def __sub__(self,other):
        self.real = self.real - other.real
        self.imag = self.imag - other.imag
        return self
    
    def __str__(self):
        return f'{self.real} + {self.imag}i'

cn1 = Complex_number(10 , 5)
cn2 = Complex_number(16 , 4)
cn3 = Complex_number(16 , 4)

print(cn1+cn2+cn3)
print(cn1-cn2-cn3)



