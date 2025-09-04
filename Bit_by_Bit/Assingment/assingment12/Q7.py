# 7. Python Program to Calculate the Length of a String Without Using a
# Library Function

def count_length(str):
    count = 0
    for ele in str:
        count+=1
    return count

str = input("Enter the string: ")
res = count_length(str)
print(f'The Length of a String is: {res}')