# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String

def count(str):
    num_char = 0
    num_word = 1
  
    for i in range(len(str)):
        if str[i].isalpha():
            num_char+=1
        else:
            if str[i].isspace():
                num_word+=1

    return num_char,num_word

str = input("Enter the string: ")
res1,res2 = count(str)
print(f'{res2} Words and {res1} Characters Present in the String')