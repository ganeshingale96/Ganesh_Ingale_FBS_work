# 5. WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input("Enter the cost price of book: "))
dis = int(input("Enter the Discount: "))
discount = (cost_price*dis)/100
sell_price = discount + cost_price
print(f'Selling price of book:{sell_price}')