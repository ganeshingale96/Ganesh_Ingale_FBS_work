# 12. Python Program to count number of lowercase characters in a string.
def count(str):
    count = 0
    #1.----------
    # for i in range(len(str)):
    #     if str[i].islower():
    #         count+=1
    # return count
    #2.----------
    for char in str:
        if ord(char)>=97:
            count+=1
    return count

str = input("Enter the string: ")
res = count(str)
print(f'{res} lowercase characters in a string')