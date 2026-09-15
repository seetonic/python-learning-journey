from bank_accounts import *

John = BankAccount(1000,"John")
kelly = BankAccount(2300, "Kelly")

John.deposit(200)
kelly.deposit(200)

John.withdraw(221)
kelly.withdraw(341)