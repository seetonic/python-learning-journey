row = int(input("enter the number of row: "))
column = int(input("enter the number of column: "))
symbol = input("enter the symbol: ")

for x in range(row):
    for y in range(column):
        print(symbol, end="")
    print()
