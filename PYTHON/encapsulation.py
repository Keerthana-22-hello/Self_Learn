class Account:
    def __init__(self,name,__balance):
        self.name=name
        self.__balance=__balance
    def deposit(self,amount):
        if amount > 0:
            self.balance  +=amount
    def getBalance(self):
        return self.__balance
    def __self_method(self):
        print("Shh..This is private")

acc=Account("Keerthana",1000)
b=acc.getBalance()
print("Balance in account : ",b)
