class AgeTooShort(Exception):
    pass

age=int(input("Enter your age : "))
if (age<18):
    raise AgeTooShort("You are too young vote..")
else:
    print("You are eligible.")