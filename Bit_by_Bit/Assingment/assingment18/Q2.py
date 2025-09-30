# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator
class Distance:
    def __init__(self,km,m,cm):
        self.km = km
        self.m = m
        self.cm = cm
    def __del__(self):
        pass
    def __add__(self,other):
        cm = self.cm + other.cm
        m = cm // 100
        self.cm = cm % 100
        m = self.m + other.m + m
        km = m //1000
        self.m = m % 1000
        self.km = self.km + other.km +km
        return self
    def __sub__(self,other):
        cm = self.cm - other.cm
        m = cm // 100
        self.cm = cm % 100
        m = self.m - other.m + m
        km = m //1000
        self.m = m % 1000
        self.km = (self.km - other.km) +km
        return self
    def __str__(self):
        return f'KM: {self.km} M: {self.m} CM:{self.cm}'

d1 = Distance(2,2000,200)
d2 = Distance(1,1000,100)
d3 = Distance(1,1000,100)
# print(d1+d2+d3)
print(d1-d2)