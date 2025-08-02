# 6. Write a program to calculate profit or loss.

cp = int(input("Enter the cost price: "))
sp = int(input("Enter the selling price: "))

p = sp-cp

if(p>0):
    print("are you in profit")
elif(cp==sp):
    print("No profit!! No loss!!")
else:
    print("are you in loss")