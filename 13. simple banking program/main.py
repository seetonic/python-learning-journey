def show_balance(balance):
     print()
     print("**************************")
     print(f"your balance is: ${balance:.2f}")
     print("**************************")
     print()

def deposit():
    amount = float(input("Enter the amount you want to deposit: $ "))
    if amount < 0:
        print("enter the valid amount.")
        return 0
    else:
        print("**************************")
        print(f"you deposit: {amount:.2f}")
        print("**************************")
        return amount
    

def withdraw(balance):
    amount = float(input("Enter the amount you want to withdraw: $ "))

    if amount < 0:
        print("enter the valid amount.")
        return 0
    elif amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        print("**************************")
        print(f"you withdraw: {amount:.2f}")
        print("**************************")
        return amount

def main():
    is_running = True

    balance = 0

    while is_running:
        print("**************************")
        print("     Banking Program     ")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("**************************")

        choice = input("Enter the choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("**************************")
            print("Invalid Input.")
            print("**************************")

    print("**************************")
    print("Thank you! Have a nice day!")
    print("**************************")

if __name__ == "__main__":
    main()