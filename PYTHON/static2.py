class TemperatureConvertor:
    @staticmethod
    def cel_to_far(a):
        return (a*(9/5))+32
    @staticmethod
    def far_to_cel(a):
        return (a-32)*(5/9)

x=int(input("Enter the celsius : "))
print("Value of celsius in Farenhiet : ",TemperatureConvertor.cel_to_far(x))
y=int(input("Enter the Farenhiet : "))
print("Value of Farenhiet in celsius : ",TemperatureConvertor.far_to_cel(y))

