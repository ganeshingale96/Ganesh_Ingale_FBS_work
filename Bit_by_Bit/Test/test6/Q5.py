
def union(set1,set2):
    li = []
    for i in (set1+set2):
        if i not in li:
            li.append(i)
    return li

set1 = (1,2,3,4,5,6)
set2 = (5,6,7,8,9,10)
print(f'Union of two list: {union(set1,set2)}')