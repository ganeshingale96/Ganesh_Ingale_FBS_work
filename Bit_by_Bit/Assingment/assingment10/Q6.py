# 6. Write a program to remove duplicates from the list.
li = [1,2,34,45,42,432,324,6,78,42,9,352,7,89,42]
unique_li = []
for ele in li:
    if ele not in unique_li:
        unique_li.append(ele)
print(unique_li)
