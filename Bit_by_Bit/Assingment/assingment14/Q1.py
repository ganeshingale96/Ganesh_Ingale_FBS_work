# 1. Write a Python program to find elements in a given set that are not in
# another set
set1 = (1,2,3,4,5,6,7,8)
set2 = (1,2,3,4,5)

if len(set1) >= len(set2):
    for ele in set1:
        if ele not in set2:
            print(ele,end=' ')
else:
    for ele in set2:
        if ele not in set1:
            print(ele,end=' ')
            










        
