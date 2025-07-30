# 7. Program to Find the Roots of a Quadratic Equation
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

sqrt = ((b**2)-(4*a*c))**0.5
result1 = (-b+sqrt)/2*a
result2 = (-b-sqrt)/2*a

print(f"The '+'result {result1} and '-'result {result2} of Quadratic Equation.")
