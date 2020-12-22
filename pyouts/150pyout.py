# Add the __init__() Funtion

class ParentClass:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class ChildClass(ParentClass):
    def __init__(self, fname, lname, age):
        ParentClass.__init__(self, fname, lname)
        #self.fname = fname
        #self.lname = lname
        self.age = age

personA = ChildClass("George", "O'nell", 65)
personB = ChildClass("John", "Gordon", 34)

print(personB.fname)
