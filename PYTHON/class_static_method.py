# class methods
'''
Feature	          |  Instance Method	                    |    Class Method
------------------|-----------------------------------------|------------------------------------------|
Bound to	      |  The object (instance)	                |    The class itself
First parameter	  |  self (refers to the instance)	        |    cls (refers to the class, not object)
Access what?	  |  Can access both instance & class vars	|    Can only access class variables
How it's called	  |  By object (obj.method())	            |    By class or object (Class.method())
-----------------------------------------------------------------------------------------------------
'''

class Student:
    schoolName="ABC School"

    @classmethod
    def changeSchoolName(cls,newName):
        cls.schoolName=newName

print("Name : "+Student.schoolName)
Student.changeSchoolName("XYZ School")
print("Name : "+Student.schoolName)


# static methods
class Calculator:
    @staticmethod
    def add(x,y):
        return x+y

print(Calculator.add(1,1))
