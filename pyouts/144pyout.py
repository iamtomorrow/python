# Modify Object Properties

class Users:
    def __init__(self, name, age):
        self.name = name
        self.age = age

userA = Users("John", 45)

# modifying my object property
userA.name = "George"

print(userA.name)
