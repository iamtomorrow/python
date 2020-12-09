# Use the super() Function

class ParentClass:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class ChildClass(ParentClass):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age

personA = ChildClass("John", "Reyes", 67)
personB = ChildClass("Murphy", "Johnson", 23)

print(personB.fname + " " + personB.lname)
