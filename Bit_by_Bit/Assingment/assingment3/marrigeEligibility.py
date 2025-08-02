# 10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input("Enter the gender (M/F): ")
age = int(input("Enter the age: "))

if ((gender == 'M' or gender == 'm') and age >= 21) or ((gender == 'F' or gender == 'f') and age >= 18):
    print("Person is eligible to marry")
else:
    print("person is not eligible to marry")