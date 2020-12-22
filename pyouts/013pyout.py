#The global keyword
#a = "fantastic"

def myFunc():
    global a 
    a = "awesome"
    print("Python is " + a)

myFunc()
print("Python is " + a)
