
import functions;
from time import sleep;

def loginOptions():
    print("WELCOME TO LOGIN SYSTEM")
    sleep(3)

    while True:
        print("-----OPTIONS-----")
        print("1 - Sign Up")
        print("2 - Sign In")
        print("3 - Exit System")
        userOption = str(input("Option: "))
        if (userOption == "1" or userOption == "2" or userOption == "3"):
            if (userOption == "1"):
                functions.signUpFunction();
            elif (userOption == "2"):
                functions.signInFunction();
            else:
                functions.exitFunction();
            break;
        else:
            print("Please you need isert a valid option! Try again.")