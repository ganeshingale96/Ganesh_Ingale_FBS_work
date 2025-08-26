# 2. Write a program to find maximum and minimum element in a list.
li = [10,2,34,45,42,432,324,6,78,9,352,7,89]
max_num = li[0]
min_num = li[0]
for i in range(1,len(li)):
    if li[i] > max_num:
        max_num = li[i]
    elif li[i] < min_num:
        min_num = li[i]
print(f'The maximum: {max_num} and minimum: {min_num}')
