# 11. Write a program to print all numbers which are divisible by m and n in the
# list.
m = int(input("Enter the M: "))
n = int(input("Enter the N: "))
li = [122,133,144,155,166,177,188,199,324,643,134,754,846,342]
for ele in li:
    if(ele%m==0 or ele%n==0) :
        print(ele)
