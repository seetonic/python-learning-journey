class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance, name):
        self.balance = initial_balance
        self.name = name

        print(f"\naccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount

        print(f"\nDeposit Completed!\n'{self.name}' Balance = ${self.balance:.2f}")

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\n Sorry, account '{self.name} only has a balance of ${self.balance:.2f}'")

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\nWithdraw Completed!")
            self.getBalance()
        except BalanceException as e:
            print(f"\nwithdraw interrupted: {e}")
