# 13 . Write a program to print list after removing even numbers.
li = [122,133,144,155,166,177,188,199,324,643,134,754,846,342]

for ele in li:
    if ele%2==0:
        li.remove(ele)
print(f'after removing even numbers: {li}')