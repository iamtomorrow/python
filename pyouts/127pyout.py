#Arbritary Keyword Arguments, **kwargs

def MyFunction(**name):
    print("the first name is", name["fname"])
    print("the last name is", name["lname"])

MyFunction(fname = "George", lname = "Biden")
