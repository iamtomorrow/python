# Delete Object Properties

class Users:
    def __init__(self, name, age):
        self.name = name
        self.age = age

userA = Users("George", 34)

# deleting object property
del userA.age

print(f"my name is {userA.name}, and I am {userA.age} years")
