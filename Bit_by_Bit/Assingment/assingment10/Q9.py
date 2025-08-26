# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#1--------------

# even_li = []
# odd_li = []
# for ele in li:
#     if ele%2==0:
#         even_li.append(ele)
#     else:
#         odd_li.append(ele)
# print(even_li)
# print(odd_li)

#2--------------
even_li = list(filter(lambda x: x%2==0 ,li))
odd_li = list(filter(lambda x: x%2!=0 ,li))
print(even_li)
print(odd_li)
print(id(even_li),id(odd_li))
