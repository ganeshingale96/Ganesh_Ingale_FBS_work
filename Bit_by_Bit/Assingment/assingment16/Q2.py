# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:
    discount = 10
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
    def cal_discount(self):
        self.dis = self.pri * Product.discount / 100
        self.final_price = self.pri-self.dis
        return f"After the discount price: {self.final_price}"


b1 = Product()
b1.show_product()
print(b1.cal_discount())
del b1
b2 = Product(109,"Ac",20000,1)
b2.show_product()
print(b2.cal_discount())


    