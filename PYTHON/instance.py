class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"Name : {self.name} \nAge: {self.age} ")

s1=Student("Keerthana",17)
s2=Student("Hemana",15)
s1.show()
s2.show()
