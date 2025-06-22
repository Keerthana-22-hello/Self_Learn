class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def describe(self):
        print("Name of the animal : ",self.name)
        print("Species :  ",self.species)

class Dog(Animal):
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed=breed
    def bark(self):
        self.describe()
        print(f"Woof!  I'm a {self.breed}")

dog1=Dog("Buji","Mammal","Labrador")
dog1.bark()

