#creating another class

class User:
    def __init__(self, name, age):
        self.aName = name
        self.aAge = age

userA = User("Elon Musk", 76)

print(userA.aName, "has ", userA.aAge)
