class Account:
    """
    This Class is for simple OOPS concepts
    """
    def __init__(self,filepath):
        with open(filepath,"r")as file:
            self.filepath=filepath
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit_balance(self):
        with open(self.filepath,"w") as file:
            file.write(str(self.balance))




"""
Use the below method to run the class 
"""

account=Account("balance.txt")
print(account.__doc__)
#print(account)
#print(account.balance)
#account.withdraw(100)
#print(account.balance)
#account.deposit(500)
#print(account.balance)
#account.commit_balance()