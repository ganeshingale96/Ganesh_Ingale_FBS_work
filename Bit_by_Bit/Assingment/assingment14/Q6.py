# 6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set
li = [3,1,2,-10,-9,8,7]

li.sort()
if li[0]*li[1]>li[-2]*li[-1]:  
    print(f'The Number {li[0]} and {li[1]} is product is maximum: {li[0]*li[1]}')
else:  
    print(f'Number {li[-1]} and {li[-2]} is product is maximum: {li[-1]*li[-2]}')