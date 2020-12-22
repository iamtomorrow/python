# Create a Child Class

class ParentClass:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class ChildClass(ParentClass):
    pass

personA = ParentClass("John", "Onell")
personB = ChildClass("George", "Omega")

print(personA.fname)
print(personB.fname)
