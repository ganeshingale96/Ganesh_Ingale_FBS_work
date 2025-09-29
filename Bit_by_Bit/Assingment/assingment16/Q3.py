# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook
class Shirt:
    each_price_change = 10
    def __init__(self,sid=1,sname="Nan",type='Nan',price=100,size='NAN'):
        self.id = sid
        self.sn = sname
        self.ty = type
        self.pri = price
        self.si = size
    def __del__(self):
        print("All Done!!")
    def show_shirt(self):
        print("Shirt Id:-",self.id)
        print("Shirt Name:-",self.sn)
        print("Shirt Type:-",self.ty)
        print("Shirt Price:-",self.pri)
        print("Shirt Size:-",self.si)

    def price_change(self):
        self.small_price = self.pri
        self.medium_price = self.small_price+((self.small_price*Shirt.each_price_change)/100)
        self.large_price = self.medium_price+((self.small_price*Shirt.each_price_change)/100)
        self.xlarge_price = self.large_price+((self.small_price*Shirt.each_price_change)/100)
        return f"small price:{self.small_price}\nmedium price:{self.medium_price}\nlarge price:{self.large_price}\nxlarge price:{self.xlarge_price}\n"
    

b1 = Shirt()
b1.show_shirt()
print(b1.price_change())
del b1
b2 = Shirt(109,"Lenan","Formal",2000,"M")
b2.show_shirt()
print(b2.price_change())
