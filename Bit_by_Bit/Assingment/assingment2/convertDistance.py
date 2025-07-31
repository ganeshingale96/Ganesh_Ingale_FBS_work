# 3. Convert distance given in feet and inches into meter and centimeter.
feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))

total_inch = (feet*12)+inches

centimeter = total_inch*2.54
meter = int(centimeter/100)
print(f'After converting distance {feet} feet and {inches} inches into {meter} meter and {centimeter} centimeter')
