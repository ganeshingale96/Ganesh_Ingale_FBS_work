# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions
def count_length(str):
    count = 0
    for ele in str:
        count+=1
    return count

def check(str1,str2):
    return count_length(str1) > count_length(str2)

str1 = input("Enter the 1st string: ")
str2 = input("Enter the 2nd string: ")
if check(str1,str2):
    print(f"First string '{str1}' is the Larger String")
else:
    print(f"Second string '{str2}' is the Larger String")