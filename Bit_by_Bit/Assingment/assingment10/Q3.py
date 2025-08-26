# 3. Write a program to find the second largest element in the list.
li = [10,2,34,45,42,432,324,6,78,9,352,7,89]
max_num = li[0]
s_max_num  = 0

for i in range(1,len(li)):
    if li[i] > max_num:
        s_max_num = max_num
        max_num = li[i]
    elif li[i] > s_max_num:
        s_max_num = li[i]

print(f'The second largest number: {s_max_num}')
