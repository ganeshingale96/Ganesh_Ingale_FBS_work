# 8. Python Program to Remove the Characters of Odd Index Values in a
# String
def remove_odd_index(str):
    new_str = ''
    for i in range(len(str)):
        if i%2==0:
            new_str += str[i] 
    return new_str

str = input("Enter the string: ")
res = remove_odd_index(str)
print(f'After remove the Odd Index Values in a string: {res}')

