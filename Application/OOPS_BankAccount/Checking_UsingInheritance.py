from account import *


class Checkin(Account):
    """
    This Class Inherites account.py and gets all the methods of it in this class along with its own object and implementation
    """
    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee

    def tansfer(self,amount):
        check.balance=check.balance-amount-self.fee

check=Checkin("balance.txt",2)
print(check.__doc__)
print(check.balance)
check.tansfer(200)
print(check.balance)
check.commit_balance()



