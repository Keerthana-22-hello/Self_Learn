def get_input():
    try:
        a=int(input("Enter a number : "))
        b=int(input("Enter another number : "))
        return a,b
    except ValueError:
        print("Invalid input. Enter only number.")

def add():
    print("Add")
    a,b=get_input()
    print("result : ",a+b)

def sub():
    print("Subtract")
    a,b=get_input()
    print("result : ",a-b)    

def mul():
    print("\nMultiply")
    a,b=get_input()
    print("result : ",a*b)
    

def div():
    print("\nDivision")
    a,b=get_input()
    if b==0:
        print("Can't divide by zero.");
        return
    print("result : ",a/b)
    

def fact():
    print("\nFactorial")
    a=int(input("Enter a number : "))
    sum=1
    for i in range (1,a+1):
        sum*=i
    print("result : ",sum)
    

def pow():
    print("\nPower")
    a,b=get_input()
    print("result : ",a**b)
    

def sq():
    print("\nSquare")
    a=int(input("Enter a number : "))
    print("result : ",a*a)
    