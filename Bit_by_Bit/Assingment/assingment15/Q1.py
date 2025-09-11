# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
class Book:
    def __init__(self,bid=1,bname="NAN",price=100,author='NAN'):
        self.id = bid
        self.bn = bname
        self.pri = price
        self.au = author
    def __del__(self):
        print("All Done!!")
    def show_book(self):
        print("Book Id:-",self.id)
        print("Book Name:-",self.bn)
        print("Book Price:-",self.pri)
        print("Book Author:-",self.au)

b1 = Book()
b1.show_book()
del b1
b2 = Book(109,"Chava",800,"Shivaji Sawant")
b2.show_book()

    