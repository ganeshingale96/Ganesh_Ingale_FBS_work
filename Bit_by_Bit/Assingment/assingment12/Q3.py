# 3. Python Program to Detect if Two Strings are Anagrams
def check_anagram(s1,s2):
    sorted_s1 = list(s1)
    sorted_s2 = list(s2)
    if len(sorted_s1)==len(sorted_s2):
        for i in range(len(sorted_s1)):
            for j in range(len(sorted_s1)-i-1):
                if sorted_s1[j]>sorted_s1[j+1]:
                    sorted_s1[j],sorted_s1[j+1]=sorted_s1[j+1],sorted_s1[j]
            for j in range(len(sorted_s2)-i-1):
                if sorted_s2[j]>sorted_s2[j+1]:
                    sorted_s2[j],sorted_s2[j+1]=sorted_s2[j+1],sorted_s2[j]
        if sorted_s1==sorted_s2:
            return True
    else:  
        return False
str1 = input("Enter the 1st string: ")
str2 = input("Enter the 2nd string: ")
res = check_anagram(str1,str2)
if res:
    print(f'The strings are Anagrams!!')
else:
    print(f'The strings are not Anagrams!!')