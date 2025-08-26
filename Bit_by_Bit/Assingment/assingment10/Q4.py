# 4. Write a program to reverse the list.
li = [1,2,34,45,42,432,324,6,78,9,352,7,89]
reverse_li = []
for i in range(1,len(li)+1):
    reverse_li.append(li[-i])
print(reverse_li,end=' ')
