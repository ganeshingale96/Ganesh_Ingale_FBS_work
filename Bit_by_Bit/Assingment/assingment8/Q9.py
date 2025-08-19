# 9. Write a program to check if entered number is a palindrome or
# not.
def check_palindrome(num):
    if (num[0]==num[2]):
        return True


n = input("Enter the number: ")
result=check_palindrome(n)
if(result):
    print(f"The {n} number is palindrome")
else:
    print(f"The {n} number is not palindrome")

