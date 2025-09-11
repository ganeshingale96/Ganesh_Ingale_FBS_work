# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook
class Shirt:
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

b1 = Shirt()
b1.show_shirt()
del b1
b2 = Shirt(109,"Lenan","Formal",2000,"M")
b2.show_shirt()