class Person:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(self.name," is speaking..")

class Student(Person):
    def study(self):
        print(self.name," is studying..")

s1=Student("Keerthana")
s1.speak()
s1.study()