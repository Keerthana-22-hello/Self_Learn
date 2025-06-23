# operator ovrerriding
# it is used to override the operators function that is built-in
class Box:
    def __init__(self,volume):
        self.volume=volume
    def __gt__(self,other):
        return self.volume > other.volume

class ADD:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return self.pages+other.pages

box1=Box(50)
box2=Box(500)
print(box1 > box2)

page1=ADD(100)
page2=ADD(200)

print(page1+page2)