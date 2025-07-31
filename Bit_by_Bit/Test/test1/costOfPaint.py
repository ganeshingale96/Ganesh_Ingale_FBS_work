area = int(input("Enter area of one wall : "))
cost_int = int(input("Enter the cost interior: "))
cost_ext = int(input("Enter the cost exterior: "))

inter_a = (10*area)*cost_int
exte_a = (6*area)*cost_ext

print(f'Cost of the Interior:{inter_a} and Exterior {exte_a} total cost is {inter_a + exte_a}')