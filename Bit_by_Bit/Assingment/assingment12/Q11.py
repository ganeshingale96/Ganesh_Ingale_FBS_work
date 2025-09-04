# 11. Python Program to replace every blank space with hyphen in a string.

def replace(str):
    new_str = ''
    for i in range(len(str)):
        if str[i] != ' ':
            new_str += str[i]
        else:
            new_str += '-'
    return new_str

str = input("Enter the string: ")
res = replace(str)
print(f'After replace Every Blank Space with Hyphen: {res}')

