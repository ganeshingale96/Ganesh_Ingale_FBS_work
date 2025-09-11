# 9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number
def unique_combination(li,target):
    li1 = []
    for i in range(len(li)):
        for j in range(i,len(li)):
            for k in range(j,len(li)):
                if li[i] != li[j] != li[k] and li[i]+li[j]+li[k] == target:
                    print(f' {li[i]} + {li[j]} + {li[k]} = {target}')

li = [1,2,3,4,5,6]
target = int(input("Enter target number: "))
unique_combination(li,target)