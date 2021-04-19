
from functionspackage import functions

# Global ariables;
menuUserOption = 0
userExitOption = 0

def system():
    print('WELCOME AIRLINES RESERVATION SYSTEM')
    
    print('-'*40)
    functions.menuOptionsFunction()

    while True:
        menuUserOption = str(input('Option: '))
        print('-'*40)
        if (str(menuUserOption).isnumeric() == False):
            while (str(menuUserOption).isnumeric() == False):
                print("The option is invalid! Try again.")
                menuUserOption = str(input("Option: "))
                if (str(menuUserOption).isnumeric() == True):
                    break;
        else:
            if (1 > int(menuUserOption) > 6):
                while (1 > int(menuUserOption) > 6):
                    print('The option ', menuUserOption, ' is invalid! Try again.')
                    menuUserOption = str(input('Option: '));
                    if (1 < int(menuUserOption) <= 6):
                        break;
            else:
                if (int(menuUserOption) == 1):
                    functions.reserveSeatFunction()
                    break;

                elif (int(menuUserOption) == 2):
                    functions.userTicketFunction()
                    break;

                elif (int(menuUserOption) == 3):
                    functions.flightScheduleFunction()
                    break;

                elif (int(menuUserOption) == 4):
                    functions.displayPassengersFunction();
                    break;

                elif (int(menuUserOption) == 5):
                    functions.flightDetailsFunction()
                    break;

                elif (int(menuUserOption) == 6):
                    functions.exitSystemFunction()
                    break;
