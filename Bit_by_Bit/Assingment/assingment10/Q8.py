# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.
li = [1,2,3,4,5,6,7,8,9,10]
#1------------
# dup_li = []
# for ele in li:
#     dup_li.append(ele)
# print(dup_li)
# print(id(li),id(dup_li))

#2------------
dup_li = list(map(lambda x: x,li))
print(id(dup_li),id(li))
