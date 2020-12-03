#Python Inheritance

class nameClass:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class ageClass(nameClass):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age

class finalClass(ageClass):
    pass

userA = finalClass("Robert", "Junior", 34)

print(f"User A: \nName: {userA.fname} {userA.lname} \nAge: {userA.age}")
