# 5. A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST
p1 = int(input("Enter the price of first product: "))
p2 = int(input("Enter the price of second product: "))
p3 = int(input("Enter the price of third product: "))
p4 = int(input("Enter the price of fourth product: "))
p5 = int(input("Enter the price of fifth product: "))

total = p1+p2+p3+p4+p5
gst = (total)*18/100

print(f'the total bill after adding 18% GST:{gst+total}')