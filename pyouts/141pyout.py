#The __init__ () Function

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

userA = User("Johnson", 56)
userB = User("Elisa", 76)

print("name: ", userA.name, "\nage: ", userA.age)
print("name: ", userB.name, "\nage: ", userB.age)
