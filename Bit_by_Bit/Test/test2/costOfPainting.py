# 4. Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.

size_wall = int(input("Enter the size of wall: "))
cost = int(input("Enter the cost of painting one wall: "))

cost = ((size_wall)*5)*cost
print(f'total cost of painting:{cost}')

