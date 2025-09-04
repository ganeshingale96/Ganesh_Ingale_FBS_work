# 6. Python Program to Multiply All the Items in a Dictionary
def mul_of_items(dic):
    mul = 1
    for itm in dic.values():
        mul *=itm
    return mul

dic = {'Apple':30,'Banana':20,'Cherry':50}
print(f'Multiply All the Items in a Dictionary: {mul_of_items(dic)}')