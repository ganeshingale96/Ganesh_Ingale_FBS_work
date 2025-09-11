# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook
class Product:
    def __init__(self,pid=1111,pname="NAN",price=100,quantity='NAN'):
        self.id = pid
        self.bn = pname
        self.pri = price
        self.au = quantity
    def __del__(self):
        print("All Done!!")
    def show_product(self):
        print("Product Id:-",self.id)
        print("Product Name:-",self.bn)
        print("Product Price:-",self.pri)
        print("Product Quantity:-",self.au)

b1 = Product()
b1.show_product()
del b1
b2 = Product(109,"Ac","20k",1)
b2.show_product()

    