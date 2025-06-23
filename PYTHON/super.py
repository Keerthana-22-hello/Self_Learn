# example of usage of super in single inheritance
class Animal:
    def Sound(self,name):
        self.name=name
        print(f"Name of the pet : {self.name}")
class dog(Animal):
    def Sound(self,name,breed):
        super().Sound(name)  # calls animal's constructor
        self.breed=breed
        print(f"Breed of the per : {self.breed}")
# example of usage of supe in method overriding
class animal:
    def sound(self,name):
        self.name=name
        print(f" {self.name} produces generic sound")
class Dog(animal):
    def sound(self,name):
        super().sound(name)
        print("bark")

d1=dog()
d1.Sound("Tommy","Labrador")
d2=Dog()
d2.sound("Buji")


