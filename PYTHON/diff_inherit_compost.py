# difference between composition and inheritance

'''
1. Inheritance “Is a” relationship
One class inherits from another.

Child class gets all the features of the parent.

Used when one class is a special type of another.
'''
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):  # dog 'is a' animal
    def bark(self):
        print("Dog barks")
d=Dog()
d.sound()  # from animal
d.bark()  # from dog

'''
 2. Composition “Has a” relationship
One class contains another class as a component.

Used when one class uses another's features.

Promotes loose coupling and more flexible design.

'''

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine=Engine()    #Car 'has a' engine 
    def start(self):
        self.engine.start()

c=Car()
c.start()

# difference table

'''
Feature	         |       Inheritance	                        |            Composition
-----------------|----------------------------------------------|---------------------------------------------
Type	         |       “Is a”	                                |           “Has a”
Coupling	     |       Tightly coupled	                    |            Loosely coupled
Flexibility	     |       Less flexible (rigid hierarchy)	    |            More flexible (replaceable parts)
Reusability	     |       Inherits everything	                |            Uses only what's needed
Example	         |       Dog → Animal	                        |            Car → Engine
--------------------------------------------------------------------------------------------------------------
'''