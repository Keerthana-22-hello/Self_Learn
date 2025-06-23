# super usage in constructor
class Animal:
    def __init__(self,name):
        self.name=name
        print(f"Name of the name : {self.name}")
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
        print("Breed of the animal")
class Father:
    def __init__(self):
        print("father")
class Mother:
    def __init_(self):
        print("Mother")
class Child(Father,Mother):
        
d1=Dog("Buji","Labrador")