# polymorphism means many forms.  In Python, it refers o the ability of different classes to 
# repond to th same method name in different ways

# polymorphism - built-in
print(len("Keerthana"))
print(len([1,2,3,4]))

# polymorphism with functions and objects
class cat:
    def sound(self):
        print("Meow")

class dog:
    def sound(self):
        print("bark")

def animal_sound(animal):   
    animal.sound()

c=cat()
d=dog()

animal_sound(c)
animal_sound(d)

# method overriding using polymorphism

class Animal:
    def move(self):
        print("Animal can move")
class Dog(Animal):
    def move(self):
        print("Dog can run and walk.")
d=Dog()
d.move()
