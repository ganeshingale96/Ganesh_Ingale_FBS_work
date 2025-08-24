# 4. Write a program to find sum of n numbers using recursion.
def sum_of_n_num(num):

    if(num==0):
        return 0
    else:
        return num+sum_of_n_num(num-1)
n = int(input("Enter the number: "))
print(sum_of_n_num(n))





