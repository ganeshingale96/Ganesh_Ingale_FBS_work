# 5. Python Program to Count the Number of Vowels in a String
def count_vowels(str):
    vowels = ['a','e','i','o','u']
    count = 0
    for char in str:
        if char in vowels:
            count+=1
    return count

str = input("Enter the string: ")
res = count_vowels(str)
print(f'The Number of Vowels in a String is: {res}')