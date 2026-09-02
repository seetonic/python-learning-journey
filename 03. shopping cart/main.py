item = input("Enter the item name: ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

total = price * quantity

print(f"your bought {quantity} X {item}/s")
print(f"your total is ${round(total,2)}")
