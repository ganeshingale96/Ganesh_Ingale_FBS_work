# 2. Write a program to input any alphabet and check whether it is vowel or consonant.

alp = input("Enter an alphabet: ")
if alp in 'aeiou':
    print(f'{alp} is a vowel')
else:
    print(f'{alp} is a consonant')
