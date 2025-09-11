# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.
set1 = {1,2,3,4,5,6,7,8,9}
li = list(set1)
for i in range(len(li)):
    for j in range(i,len(li)):
        if li[i] + li[j]==10:
            print(li[i],li[j])
