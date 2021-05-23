
import functions;
from time import sleep;
import os;

def formatFunction(txt):
    print("-"*20, txt, "-"*20, "\n\n");
def formatMenuFunction(txt):
    print(" "*20, txt);

def systemFunction():
    os.system("cls")
    formatFunction("CUSTOMER ACCOUNT BANKING MANAGEMENT SYSTEM");

    formatFunction('MAIN MENU');
    formatMenuFunction("1 - Create New Account");
    formatMenuFunction("2 - Create New Bank Account");
    formatMenuFunction("3 - Update Information Of Existing Account");
    formatMenuFunction("4 - For Transactions");
    formatMenuFunction("5 - Check Details Of Existing Account");
    formatMenuFunction("6 - Remove Account");
    formatMenuFunction("7 - View Customer's List");
    formatMenuFunction("8 - Exit System");

    while True:
        option = str(input("Option: "));
        if ("1" <= option <= "7"):
            if (option == "1"):
                functions.createAccountFunction();
                break;
            elif (option == "2"):
                functions.createBankAccount();
                break;
            elif (option == "3"):
                functions.updateInfoFunction();
                break;
            elif (option == "4"):
                functions.transactionsFunction();
                break;
            elif (option == "5"):
                functions.checkDetailsFunction();
                break;
            elif (option == "6"):
                functions.removeAccountFunction();
                break;
            elif (option == "7"):
                functions.viewCustomerListFunction();
                break;
            elif (option == "8"):
                functions.exitSystemFunction();
                break;
        else:
            print("Please, you need insert a valid option. Try again.");
            sleep(2);
