# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)
sub1 = int(input("Enter the marks of First Subject: "))
sub2 = int(input("Enter the marks of Second Subject: "))
sub3 = int(input("Enter the marks of Third Subject: "))
sub4 = int(input("Enter the marks of Fourth Subject: "))
sub5 = int(input("Enter the marks of Fifth Subject: "))

marks_per = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

if marks_per >= 60:
    print("First Class")
elif marks_per >= 50:
    print("Second Class")
elif marks_per >= 40:
    print("Third Class")
else:
    print("Fail")

