class School:
    schoolName="St. Thomas Group of Schools"
    def __init__(self,studentName):
        self.studentName=studentName
    @classmethod
    def change_SchoolName(cls,new_name):
        cls.schoolName=new_name
    def show(self):
        print(f"Name : {self.studentName} \nSchool : {School.schoolName}")

s1=School("Keerthana")
s2=School("Hemana")

s1.show()
s2.show()

School.change_SchoolName("Rajlakshmi Institute of Technology")
print("\nAfter Change\n")
s1.show()
s2.show()
