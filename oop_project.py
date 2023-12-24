from bank_account import *

Dave = BankAccount(1000 ,"Dave")
Sara = BankAccount(2000 ,"Sara")


Dave.getBalance()
Sara.getBalance()


Dave.deposit(500)
Sara.deposit(100)

Dave.withdraw(10)

Dave.transfer(10000,Sara)