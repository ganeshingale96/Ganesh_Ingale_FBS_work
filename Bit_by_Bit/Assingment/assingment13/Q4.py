# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x)
def nNum_dic(num):
    dic = {}
    for i in range(1,num+1):
        dic[i]=i**i
    return dic

num = int(input("Enter the number: "))
print(nNum_dic(num))