class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def mul(a,b):
        return a*b

x=int(input("Number 1 : "))
y=int(input("Number 2 : "))
print("Addition : ",MathUtils.add(x,y))
print("Multiplication : ",MathUtils.mul(x,y))
