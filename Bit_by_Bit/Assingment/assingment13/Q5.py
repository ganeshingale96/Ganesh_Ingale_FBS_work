# 5. Python Program to Sum All the Items in a Dictionary
def sum_of_items(dic):
    sum = 0
    for itm in dic.values():
        sum +=itm
    return sum

dic = {'Apple':30,'Banana':20,'Cherry':50}
print(f'Sum All the Items in a Dictionary: {sum_of_items(dic)}')