# 12. Write a program to create three lists of numbers, their squares
# and cubes
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#1---------

# sq_li = []
# cu_li = []

# for ele in li:
#     if ele :
#         sq_li.append(ele**2)
#         cu_li.append(ele**3)
# print(f'List: {li}')
# print(f'Squared List: {sq_li}')
# print(f'cube List: {cu_li}')

#2-------------
sq_li = list(map(lambda x: x**2, li))
cu_li = list(map(lambda x: x**3, li))
print(f'List: {li}')
print(f'Squared List: {sq_li}')
print(f'cube List: {cu_li}')


