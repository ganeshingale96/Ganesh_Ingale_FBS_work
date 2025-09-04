# 8. Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary

def count_fq_words(str):
    dic = {}
    for char in str:
        if char in dic:
            dic[char]+= 1
        else:
            dic[char] = 1
    return dic
str = 'ganegsh'
print(count_fq_words(str))
