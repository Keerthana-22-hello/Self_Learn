class Pen:
    def write(self):
        print("Pen cannot be erased.")
class Pencil:
    def write(self):
        print("Pencil can be erased.")
def tool_write(tool):
    tool.write()

p=Pen()
pe=Pencil()

tool_write(p)
tool_write(pe)

class Bird():
    def fly(self):
        print("Bird is flying..")
class Penguin(Bird):
    def fly(self):
        print("Penguin..")

peng=Penguin()
peng.fly()