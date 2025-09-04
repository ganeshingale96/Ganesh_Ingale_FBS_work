# 1. Python Program to Replace all Occurrences of ‘a’ with $ in a String
def replace(str):
    new_str = ''
    for i in range(len(str)):
        if str[i] != 'a':
            new_str += str[i]
        else:
            new_str += '$'
    return new_str

str = input("Enter the string: ")
print(replace(str))

