# 4. Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

def exchange(str):
    new_str = ''
    new_str = str[len(str)-1]+str[1:len(str)-1]+str[0]
    return new_str

str = input("Enter the string: ")
res = exchange(str)
print(f'After The Exchage First Character and Last Character Of String: {res}')
