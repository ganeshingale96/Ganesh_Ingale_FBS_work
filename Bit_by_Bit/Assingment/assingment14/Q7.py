# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

def compair_sets(set1,set2):
    miss_set2 = set()
    miss_set1 = set()
    for ele in set1:
        if ele not in set2:
            miss_set2.add(ele)
    for ele in set2:
        if ele not in set1:
            miss_set1.add(ele)
    return miss_set2,miss_set1

set1 = {1,2,3,4,5,6,7,8}
set2 = {1,2,3,24,35,56,77,88}
miss_set2,miss_set1 = compair_sets(set1,set2)

print(f'missing ele in set2: {miss_set2}')
print(f'missing ele in set1: {miss_set1}')

