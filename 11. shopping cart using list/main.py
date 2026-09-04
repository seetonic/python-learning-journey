foods = []
prices = []
total = 0

while True:
    food = input("what would you like to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food} (q to quit):$ "))
        foods.append(food)
        prices.append(price)
        if food.lower() == "q":
            break

print()
print("======= YOUR CART =======")

for food in foods:
    print(food)

for price in prices:
    total += price

print()
print(f"your total is: ${total}")
