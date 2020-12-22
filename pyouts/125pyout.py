#Arbitrary Arguments, *args

def MyFunction(*names):
    print("the yougest people present here is " + names[1])

MyFunction("Carl", "Stephen", "Neil")
