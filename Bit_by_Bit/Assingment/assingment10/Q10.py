# 10. Write a program to remove all occurrences of a given element in the list.
ele = int(input("Enter the element you want to remove from list: "))
li = [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1]
for i in range(0,len(li)):
    if ele in li:
        li.remove(ele)

print(li)