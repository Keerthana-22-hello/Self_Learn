'''
Decorator is a function that takes another function as a input, adds some functionality 
and returns the modified function - without changing the original function's structure
'''
def decorator_function(original_function):   # Creating a function with parameter  and this function will be decorated later using wrapped fujnction
    def wrapped_function():
        print("this is before calling original function...")
        original_function()
        print('This is after calling the original function')
    return wrapped_function
@decorator_function   # before running the display function pass it through  decorator_function
def display():
    print("Display function id running....")
class student():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display_info(self):
        print(f"Name : {self.name} \n Age : {self.age}")
display()
s1=student("Keerthana",17)
s1.display_info()
