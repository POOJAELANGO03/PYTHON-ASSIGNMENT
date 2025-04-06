item1 = float(input("Enter the price of item 1: "))
item2 = float(input("Enter the price of item 2: "))
item3 = float(input("Enter the price of item 3: "))
total = item1 + item2 + item3
if total > 500:
    discount = total * 0.10
else:
    discount = 0
final_amount = total - discount
print("\nTotal Price: $", total)
print("Discount Applied: $", discount)
print("Final Amount to Pay: $", final_amount)