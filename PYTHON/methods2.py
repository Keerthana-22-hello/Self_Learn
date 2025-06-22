class Library:
    libraryName="City public library"
    def __init__(self,book,author):
        self.book=book
        self.author=author
    @classmethod
    def change_libraryName(cls,newName):
        cls.libraryName=newName
    def show(self):
        print(f"Book : {self.book}\n Author : {self.author}\nLibrary : {Library.libraryName}")

s1=Library("Wings Of Fire","Dr. APJ. Abdul Kalam")
s2=Library("The Achemist","Anonymous")

s1.show()
s2.show()

Library.change_libraryName("National Digital Library")
print("\nafter change\n")
s1.show()
s2.show()
