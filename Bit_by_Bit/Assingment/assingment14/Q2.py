# 2. Write a Python program to remove the intersection of a second set
# with a first set.
def remove_intersect(set1,set2):
    set2.difference_update(set1)
    return set2

set1 = {1,2,3,4,5}
set2 = {19,20,3,4,5}

print(f'After the remove the intersection of a second set with first set: {remove_intersect(set1,set2)}')