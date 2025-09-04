# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String
def remove_nth_index(str,ind):
    new_str = ''
    new_str = str[:ind]+'$'+str[ind+1:]
    return new_str

str = input("Enter the string: ")
ind = int(input("Enter the index you want to remove from string: "))
res = remove_nth_index(str,ind)
print(f'After remove the nth Index Character from a Non-Empty string: {res}')





