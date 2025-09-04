# 1. Python Program to Add a Key-Value Pair to the Dictionary

def add_keys_values(num):
    dic = {}
    for i in range(num):
        keys = input("Enter the keys: ")
        values = input("Enter the values: ")
        dic[keys]=values
    return dic
num = int(input("Enter the nunber of key-values pair you want to add in dictionary: "))
print(f'Dictionary = {add_keys_values(num)}')