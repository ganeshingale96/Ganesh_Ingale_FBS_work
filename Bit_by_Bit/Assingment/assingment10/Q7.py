# 7. Write a program to create a new list from existing list which contains cube of
# each number of list.

# li = [1,2,3,4,4,5,6,7,8,9,0,6434,212,121]

# new_li = list(map(lambda x: x**3 ,li))
# print(new_li)

li = [1,2,3,4,4,5,6,7,8,9,6434,212,121]
print(li)
count = 0
for ele in li:
    li[count]=ele**3
    count+=1
print(li)
