class Account:
    def __init__(self,name,__balance):
        self.name=name
        self.__balance=__balance
    def withdraw(self,amount):
        self.__balance-=amount
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount    
    def getBalance(self):
        return self.__balance

acc=Account("Hemana",15000)

acc.deposit(1000)
w=int(input("Money to withdraw: "))
if (w < acc.getBalance()):
    acc.withdraw(w)
else:
    print("You don't have enough amount..  PLease deposit to withdraw")
print("In ",acc.name," account : ")
print("Balance available after withdraw : ",acc.getBalance())

