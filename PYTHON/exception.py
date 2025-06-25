# try and except and finally 
try:
    a=int(input("Enter a number : "))
    b=int(input("Enter another number : "))
    print(a/b)
except ValueError:
    print("Value error..")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    c=input("Would you like to division again : [y/n]")
    if c=='y':
        a=int(input("Enter a number : "))
        b=int(input("Enter another number : "))
        print(a/b)
    else:
        print("Thanks for the visit..")

# raise

print()
a=int(input("Enter your age : "))
if (a<18):
    raise ValueError("You are under age limit..")
else:
    print("You are eligible.")

#assert
mark=int(input("Enter your marks : "))
assert mark<=100 and mark>=0, "Invalid marks"
print("Marks are valid")