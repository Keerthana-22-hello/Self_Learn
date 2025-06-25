# property decorators

#using (@property)getter

class Student:
    def __init__(self,name):
        self._name=name
    
    @property
    def name(self): # LOOKS LIKE A METHOD BUT BEHAVES LIKE A VARIABLE
        return self._name
    
s = Student("Keerthana")
print(s.name) # has no parentheses

# using @property(setter)
class student:
    def __init__(self,name2):
        self._name2=name2
    @property
    def name2(self):
        return self._name2
    @name2.setter
    def name2(self,value):
        if len(value) < 3:
            print("Name is too short.")
        self._name2=value

s=student("Keerthana")
s.name2="KIKI"  # Calling the name2 funciton but printing hte setter function
print(s.name2)

# using @property deleter
class Student2:
    def __init__(self,name3):
        self._name3=name3
    
    @property
    def name3(self):
        return self.name3
    
    @name3.deleter
    def name3(self):
        del self._name3
        print("Name deleted")

s=Student2("Keerthana")
del s.name3   # calling the function but printing the deleter function
