from bank_accounts import *

John = BankAccount(1000,"John")
kelly = BankAccount(2300, "Kelly")

John.deposit(200)
kelly.deposit(200)

John.withdraw(221)
kelly.withdraw(341)

John.transfer(100, kelly)

Jim = InterestRewardAcc(1000, "Jim")
Jim.deposit(200)
Jim.transfer(4000, John)
Jim.transfer(400, John)

Dave = SavingAcc(1000, "Dave")
Dave.deposit(100)
Dave.transfer(10000, kelly)
Dave.transfer(1000, kelly)

