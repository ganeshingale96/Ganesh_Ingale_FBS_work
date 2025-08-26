# 5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.
li = [1,2,34,45,42,432,324,6,78,42,9,352,7,89,42]
num = int(input("Enter the number to check: "))
count = 0
for i in range(1,len(li)):
    if num == li[i]:
        count+=1
if count>0:
    print(f'The {num} present in the list')
    print(f'{count} times it is present in the list.')