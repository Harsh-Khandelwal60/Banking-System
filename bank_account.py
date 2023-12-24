class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self ,initialAmmount, accName) :
        self.balance = initialAmmount
        self.name = accName
        print(f"\nAccount'{self.name}' created.\nBalance=${self.balance:.2f}")
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    def deposit(self,amount):
        self.balance += amount
        print(f"\nDeposit Complete.")
        self.getBalance()
        
    def viableTransaction(self,amount):
        if self.balance >= amount:
            return 
        else:
            raise BalanceException(
                f"Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    
    def withdraw(self , amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"\nWithdraw complete.")
            self.getBalance()
        except BalanceException as Error:
            print(f"Withdraw interrupted: {Error}")
            
    def transfer(self , amount, account):
        try:
            print(f"**********\n\nBeginning Transfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer complete! \n\n********")
        except BalanceException as Error:
            print(f"\nTransfer interrupted!❌ {Error}")