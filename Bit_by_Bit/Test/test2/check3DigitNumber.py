# Write a program to accept 3 digit number. If first digit is double of second digit and half of
# third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
# Eg : - 428 , 214 etc.
num = int(input("Enter the number: "))
temp = num

d3 = temp%10
temp = temp//10
d2 = temp%10
d1 = temp//10



if((d1/2==d2) and (d1==d3/2)):
    print("yes,you have done")
else:
    print("Please try next time")
