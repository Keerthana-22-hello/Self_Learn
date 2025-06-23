# Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started..")
class Bike(Vehicle):
    def start(self):
        print("Bike started..")

c=Car()
c.start()

b=Bike()
b.start()