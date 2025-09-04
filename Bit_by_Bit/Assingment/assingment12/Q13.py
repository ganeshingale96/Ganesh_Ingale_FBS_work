# 13. Python Program to count number of digits and letters in a string.
def count(str):
    count_alp = 0
    count_dig = 0
    for i in range(len(str)):
        if str[i].isalpha():
            count_alp+=1
        elif str[i].isdigit():
            count_dig+=1
    return count_alp , count_dig


str = input("Enter the string: ")
res1,res2 = count(str)
print(f'{res2} digits and {res1} letters present in string')