
import enum
from sys import setprofile
import database
import os;
import system;
from time import sleep;
from money import Money;
# import pycountry;
from datetime import datetime, timezone, tzinfo

actualDate = datetime.now();
actualYear = datetime.now().year;
actualMonth = datetime.now().month;
actualDay = datetime.now().day;
customerID = 0;
dateBecomeCustomer = actualDate.now();
customerName = '';
custFisrtName = '';
custSecondName = '';
custLastName = '';
customerBirthdate = '';
customerAge = 0;
custBirthDay = '';
custBirthMonth = '';
custBirthYear = '';
customerCountry = '';
customerCountryOfficialName = '';
customerCity = '';
customerEmailAddress = '';
customerPhoneNumber = '';
customerCitizenNumber = '';
customerUsername = '';
customerPassword = '';
monetaryUnit = '';
depositAmount = '';
date = '';
accountNumber = '';
customerLoginCode = '';
accountState = ' ';
currentNumberOfTransactions = 0;
limitNumberOfTransactions = 0;
accountGrade = '';


def formatFunction(txt):
    print("-"*20, txt, "-"*20, "\n\n");
def formatMenuFunction(txt):
    print(" "*20, txt);

def createAccountFunction():
    os.system("cls");
    formatFunction("CREATE ACCOUNT");

    customerID = database.getNewCustomerID();

    while True:
        os.system("cls");
        formatFunction("NAME");
        customerName = str(input("Enter Name: ")).strip().split();
        if len(customerName) == 3:
            custFisrtName = customerName[0].capitalize();
            custSecondName = customerName[1].capitalize();
            custLastName = customerName[-1].capitalize();
            break;
        else:
            print("Please, you need insert a valid name! Try again.");

    while True:
        os.system("cls");
        formatFunction("BIRTHDATE");
        formatFunction("YEAR");
        custBirthYear = str(input("Enter Year (YYYY): "));
        if len(custBirthYear) == 4 and custBirthYear < str(actualYear):

            while True:
                os.system("cls");
                formatFunction("BIRTHDATE");
                formatFunction("MONTH");
                custBirthMonth = str(input("Enter Month: "));
                if len(custBirthMonth) == 2 and "01" <= custBirthMonth <= "12":

                    while True:
                        os.system("cls");
                        formatFunction("BIRTHDATE");
                        formatFunction("DAY");
                        custBirthDay = str(input("Enter Day: "));
                        if len(custBirthDay) == 2 and "01" <= custBirthDay <= "31":

                            custBirthDate = datetime(int(custBirthYear), int(custBirthMonth), int(custBirthDay));
                            customerAge = actualYear - int(custBirthYear);
                            if actualMonth < int(custBirthMonth):
                                customerAge -= 1;
                            elif actualMonth == int(custBirthMonth):
                                if actualDay >= int(custBirthDay):
                                    customerAge += 1;
                            else:
                                customerAge += 1;
                            break;
                        else:
                            print("Please, you need insert a valid day! Try again");
                            sleep(2);
                    break;
                else:
                    print("Please, you need insert a valid month! Try again.");
                    sleep(2);
            break;
        else:
            print("Please, you need insert a valid year! Try again.");
            sleep(2);

    while True:
        os.system("cls");
        formatFunction("COUNTRY");
        customerCountry = str(input("Enter Country: ")).strip().capitalize();
        if len(customerCountry) > 0:
            break;
        else:
            print("Please, you need insert a valid country name! Try again.");
            sleep(2);
    
    while True:
        os.system("cls");
        formatFunction("CITY");
        customerCity = str(input("Enter City: ")).strip().capitalize();
        if len(customerCity) > 0:
            break;
        else:
            print("Please, you need insert a valid city name! Try again.");
            sleep(2);

    while True:
        os.system("cls");
        formatFunction("PHONE");
        customerPhoneNumber = str(input("Enter Phone: ")).strip();
        if len(customerPhoneNumber) > 0:
            break;
        else:
            print("Please, you need insert a valid phone number! Try again.");
            sleep(2);

    while True:
        os.system("cls")
        formatFunction("EMAIL ADDRESS")
        customerEmailAddress = str(input("Enter Email: "));
        if len(customerEmailAddress) >= 6 and '@' in customerEmailAddress and '.' in customerEmailAddress:
            break;
        else:
            print("Please, you need insert a valid email address! Try again.");
            sleep(2);

    while True:
        os.system("cls")
        formatFunction("CITIZEN NUMBER")
        customerCitizenNumber = str(input("Enter Citizen Number: "));
        if len(customerCitizenNumber) > 0:
            break;
        else:
            print("Please, you need insert a valid citizen number! Try again.");
            sleep(2);
            
    while True:
        os.system("cls");
        formatFunction("USERNAME");
        customerUsername = str(input("Enter Username: ")).lower().strip().lower();

        count = 0;
        for i in range (0, len(customerUsername)):
            if customerUsername[i] == ' ':
                count += 1;
        if len(customerUsername) > 0 and count == 0 and database.confirmNewUsername(customerUsername) == True:
            break;
        else:
            if len(customerUsername) == 0:
                print("Please, you need insert a username before continue! Try again.");
                sleep(2);
            elif count > 0:
                print("Sorry, spaces between letters are not allowed! Try again.");
                sleep(2);
            elif database.confirmNewUsername(customerUsername) == False:
                print("It looks like already exists a customer with this username! Try another.");
                sleep(2);

    while True:
        os.system("cls");
        formatFunction("PASSWORD");
        customerPassword = str(input("Enter Password: "));
        if len(customerPassword) >= 10 and len(customerPassword) <= 30:
            break;
        else:
            print("Please, your password needs to have more than 9 characters or less than 31! Try again.");
            sleep(2);

    while True:
        os.system("cls");
        formatFunction("CREATE BANK ACCOUNT");
        print ("1 - Yes\n2 - Not");
        userOption = str(input("Option: "));
        if userOption == "1" or userOption == "2":
            if userOption == "1":
                print("Let's create a account...");
                sleep(3)

                while True:
                    os.system("cls");
                    formatMenuFunction("MONETARY UNIT");
                    monetaryUnit = str(input("Enter Moneatry Unit (USD Recommended): "));
                    if len(monetaryUnit) == 3:
                        
                        while True:
                            os.system("cls");
                            depositAmount = str(input(f"Enter Deposit Amount: {monetaryUnit} "));
                            if len(depositAmount) > 0 and depositAmount > "0":

                                # creating customer bank account due its initial deposit amount;
                                os.system("cls");
                                formatFunction("CREATE BANK ACCOUNT");
                                print("USD 1 > USD 4,999 | GRADE: Basic | Transactions: 5");
                                sleep(0.5);
                                print("USD 5,000 > USD 9,999 | GRADE: Standart | Transactions: 10");
                                sleep(0.5);
                                print("USD 10,000 > USD 19,999 | GRADE: Patreon | Transactions: 15");
                                sleep(0.5);
                                print("USD 20,000 > USD 49,999 | GRADE: Premium | Transactions: 20");
                                sleep(0.5);
                                print("USD 50,000 > 99,999 | GRADE: Orion | Transactions: 30");
                                sleep(0.5);
                                if 1 <= int(depositAmount) <= 4999:
                                    accountGrade = "Basic";
                                    limitNumberOfTransactions = 5;
                                elif 5000 <= int(depositAmount) <= 9999:
                                    accountGrade = "Standart";
                                    limitNumberOfTransactions = 10;
                                elif 10000 <= int(depositAmount) <= 19999:
                                    accountGrade = "Patreon";
                                    limitNumberOfTransactionss = 15;
                                elif 20000 <= int(depositAmount) <= 49999:
                                    accountGrade = "Premium";
                                    limitNumberOfTransactions = 20;
                                else:
                                    accountGrade = "Orion";
                                    limitNumberOfTransactions = 30;

                                while True:
                                    os.system("cls");
                                    formatFunction("ACOUNT NAME");
                                    accountName = str(input("Account name: "));
                                    if len(accountName) > 0:
                                        break;
                                    else:
                                        print("Please, you need insert a valid account name! Try again.");

                                while True:
                                    os.system("cls")
                                    formatFunction("ACCOUNT CODE")
                                    accountCode = str(input("Account code: "));
                                    if len(accountCode) >= 10:
                                        break;
                                    else:
                                        print("Please, your account code must have at least 10 characters! Try again.");
                                        sleep(3);

                                while True:
                                    os.system("cls");
                                    formatFunction("ACCOUNT NUMBER");
                                    accountNumber = str(input("Account number: "));
                                    if len(accountNumber) == 10:
                                        break;
                                    else:
                                        print("Please, the account number must have at least 10 characters! Try again.");

                                break;
                            else:
                                print("Please, you need insert a valid deposit amount! Try again.");
                                sleep(2);
                        break;
                    else:
                        print("Monetary unit invalid! Try again.");
                        sleep(2);
            else:
                depositAmount = 0;
                print("REMEMBER! You still don not have a account in our bank! For that, you need insert a initial deposit.");
                break;
            break;
        else:
            print("The option is invalid! Try again.");
            sleep(2);


    os.system("cls");
    print(" ");
    formatFunction("CUSTOMER INFORMATION");
    print("CUSTOMER NAME: ", custFisrtName, custSecondName, custLastName);
    sleep(0.5);
    print("CUSTOMER BIRTHDATE: ", custBirthYear, "-", custBirthMonth, "-", custBirthDay);
    sleep(0.5);
    print("CUSTOMER AGE: ", customerAge);
    sleep(0.5);
    print("CUSTOMER COUNTRY: ", customerCountry);
    sleep(0.5);
    print("CUSTOMER CITY: ", customerCity);
    sleep(0.5);
    print("CUSTOMER EMAIL: ", customerEmailAddress);
    sleep(0.5);
    print("CUSTOMER PHONE: ", customerPhoneNumber);
    sleep(0.5);
    print("CUSTOMER CITIZEN NUMBER: ", customerCitizenNumber)
    sleep(0.5);
    print("CUSTOMER USERNAME: ", customerUsername);
    sleep(0.5);
    print("CUSTOMER PASSWORD: ", customerPassword);
    sleep(0.5);
    if depositAmount != 0:
        print("DEPOSIT AMOUNT: ", depositAmount);
        sleep(0.5);
        print("ACCOUNT GRADE: ", accountGrade);
        sleep(0.5);
        print("TRANSACTIONS LIMIT: ", limitNumberOfTransactions);

        accountID = database.createBankAccount.getNewAccountID(database.createBankAccount);
        accountState = "Opened";
    else:
        print("NO INITIAL DEPOSIT AMOUNT");

    database.insertCustomerToDatabase(customerID, custFisrtName, custSecondName, custLastName, custBirthDate, customerCountry, customerCity, customerPhoneNumber, customerEmailAddress, customerAge, dateBecomeCustomer, customerCitizenNumber, customerUsername, customerPassword)
    if depositAmount != 0:
        database.createBankAccount.createAccount(database.createBankAccount, accountID, accountName, dateBecomeCustomer, accountCode, depositAmount, depositAmount, limitNumberOfTransactions, currentNumberOfTransactions, customerID, accountState, accountGrade, accountNumber);

    while True:
        print("\n1 - Exit\n2 - Main Menu");
        userOption = str(input("Option: "));
        if (userOption == "1"):
            break;
        elif (userOption == "2"):
            system.systemFunction();
        else:
            print("Please, insert a valid option! Try again.");

def createBankAccount():
    while True:
        os.system("cls");
        formatFunction("CREATE BANK ACCOUNT");
        customerCitizenNumber = str(input("Login code / Citizen number: "));
        customerPassword = str(input("Password: "));
        if database.findCustomerAccountFromCitizenNumber(customerCitizenNumber, customerPassword) == True:
            sleep(3);

            while True:
                os.system("cls");
                formatFunction("CREATE BANK ACCOUNT");
                depositAmount = str(input(f"Enter Deposit Amount: {monetaryUnit} "));
                if len(depositAmount) > 0 and depositAmount > "0":
                    break;
                else:
                    print("Please, you need create a deposit to be able to create a new bank account! Try again.");

            break;
        else:
            print("Sorry, it looks like your citizen number is not register in the bank or you entered a wrong password! Consider review the information and try again.");
            sleep(3);


def updateInfoFunction():
    # find the customer by its username and password;
    while True:
        newUsername = '';
        newPassword = '';

        os.system("cls");
        formatFunction("UPDATE INFORMATION");
        customerUsername = str(input("Enter username: "));
        if database.findCustomerUsernameFromDatabase(customerUsername) == True:

            while True:
                os.system("cls");
                formatFunction("UPDATE INFORMATION");
                customerPassword = str(input("Enter password: "));
                if database.findCustomerPasswordFromDatabase(customerUsername, customerPassword) == True:
                    print("Signed In");
                    sleep(0.5);

                    # update name;
                    while True:
                        os.system("cls");
                        formatFunction("UPDATE NAME");
                        print("1 - Yes\n2 - Not")
                        option = str(input("Option: "));
                        if option == "1" or option == "2":
                            if option == "1":
                                while True:
                                    os.system("cls");
                                    formatFunction("UPDATE NAME");
                                    customerName = str(input("Update name: ")).strip().split();
                                    if len(customerName) >= 3:
                                        newFirstName = customerName[0];
                                        newSecondName = customerName[1];
                                        newLastName = customerName[-1];
                                        database.updateCustomer.updateCustomerName(database.updateCustomer, newFirstName, newSecondName, newLastName, customerUsername);
                                        break;
                                    else:
                                        print("Please, you need insert a valid name! Try again.");
                                        sleep(2);
                            else:
                                break;

                            break;
                        else:
                            print("Please, you need insert a valid option! Try again.");
                            sleep(2);
                    
                    # update birthdate;
                    while True:
                        os.system("cls");
                        formatFunction("UPDATE BIRTHDATE");
                        print("1 - Yes\n2 - Not")
                        option = str(input("Option: "));
                        if option == "1" or option == "2":
                            if option == "1":
                                while True:
                                    os.system("cls");
                                    formatFunction("UPDATE YEAR");
                                    custBirthYear = str(input("Year (YYYY): "));
                                    if len(custBirthYear) == 4:

                                        while True:
                                            os.system("cls");
                                            formatFunction("UPDATE MONTH");
                                            custBirthMonth = str(input("Month (MM): "));
                                            if len(custBirthMonth) == 2 and "01" <= custBirthMonth <= "12":

                                                while True:
                                                    os.system("cls");
                                                    formatFunction("UPDATE DAY");
                                                    custBirthDay = str(input("Day (DD: "));
                                                    if len(custBirthDay) == 2 and "01" <= custBirthDay <= "31":
                                                        newBirthdate = datetime(int(custBirthYear), int(custBirthMonth), int(custBirthDay));
                                                        
                                                        newAge = actualYear - int(custBirthYear);
                                                        if actualMonth < int(custBirthMonth):
                                                            newAge -= 1;
                                                        elif actualMonth == int(custBirthMonth):
                                                            if actualDay >= custBirthDay:
                                                                newAge += newAge;
                                                        else:
                                                            newAge += 1;
                                                        
                                                        database.updateCustomer.updateCustomerBirthdateAndAge(database.updateCustomer, newBirthdate, newAge, customerUsername);

                                                        break;
                                                    else:
                                                        print("Please, you need insert a valid birthdate! Try again.");
                                                break
                                            else:
                                                print("Please, you need insert a valid month! Try again.");
                                                sleep(2)
                                        break;
                                    else:
                                        print("Please, you need insert a valid year! Try again.");
                                        sleep(2)
                                break;
                            else:
                                break;
                        else:
                            print("Please, you need insert a valid option! Try again.");
                            sleep(2);

                    # update country and city;
                    while True:
                        os.system("cls");
                        formatFunction("UPDATE COUNTRY");
                        print("1 - Yes\n2 - Not")
                        option = str(input("Option: "));
                        if option == "1" or option == "2":
                            if option == "1":
                                while True:
                                    os.system("cls");
                                    formatFunction("UPDATE COUNTRY");
                                    customerCountry = str(input("Update country: ")).strip();
                                    if len(customerCountry) > 0:
                                        
                                        while True:
                                            os.system("cls");
                                            formatFunction("UPDATE CITY ");
                                            customerCity = str(input("Update city: "));
                                            if len(customerCity) > 0:
                                                database.updateCustomer.updateCustomerCountry(database.updateCustomer, customerCountry, customerUsername);
                                                database.updateCustomer.updateCustomerCity(database.updateCustomer, customerCity, customerUsername);
                                                locationUpdated = True;
                                                break;
                                            else:
                                                print("Please, your ancient city should be changed due your new country! Try again.");
                                                sleep(2);
                                        break;
                                    else:
                                        print("Please, you need insert a valid country! Try again.");
                                        sleep(2);
                                break;
                            else:
                                locationUpdated = False;
                                break;
                        else:
                            print("Please, you need insert a valid option! Try again.");
                            sleep(2);
                        
                    # update only city;
                    if locationUpdated == False:
                        while True:
                            os.system("cls");
                            formatFunction("UPDATE CITY");
                            print("1 - Yes\n2 - Not");
                            option = str(input("Option: "));
                            if option == "1" or option == "2":
                                if option == "1":

                                    while True:
                                        os.system("cls");
                                        formatFunction("UPDATE CITY");
                                        customerCity = str(input("Update city: "));
                                        if len(customerCity) > 0:
                                            database.updateCustomer.updateCustomerCity(database.updateCustomer, customerCity, customerUsername);
                                            break;
                                        else:
                                            print("Please, you need insert a valid city! Try again.");
                                else:
                                    break;
                                break;
                            else:
                                print("Please, you need insert a valid option! Try again.");
                                sleep(2);
                    else:
                        break;

                    # update phone number
                    while True:
                        os.system("cls");
                        formatFunction("UPDATE PHONE NUMBER");
                        print("1 - Yes\n2 - Not");
                        option = str(input("Option: "));
                        if option == "1" or option == "2":
                            if option == "1":
                                
                                while True:
                                    os.system("cls");
                                    formatFunction("UPDATE PHONE NUMBER");
                                    customerPhoneNumber = str(input("Update phone number: "));
                                    if len(customerPhoneNumber) > 0:
                                        database.updateCustomer.updateCustomerPhoneNumber(database.updateCustomer, customerPhoneNumber, customerUsername);
                                        break;
                                    else:
                                        print("Please, you neeed insert a valid phone number! Try again.");
                                        sleep(2);
                            else:
                                break;
                            break
                        else:
                            print("Please, you need insert a valid option! Try again.");
                            sleep(2);

                    # update email address;
                    while True:
                        os.system("cls");
                        formatFunction("UPDATE EMAIL ADDRESS");
                        print("1 - Yes\n2 - Not");
                        option = str(input("Option: "));
                        if option == "1" or option == "2":
                            if option == "1":
                                while True:
                                    os.system("cls")
                                    formatFunction("UPDATE EMAIL ADDRESS");
                                    customerEmailAddress = str(input("Update email address: "));
                                    if '@' in customerEmailAddress and '.' in customerEmailAddress:
                                        database.updateCustomer.updateCustomerEmailAddress(database.updateCustomer, customerEmailAddress, customerUsername);
                                        break;
                                    else:
                                        print("Sorry, the email address entered does not corresponds to a valid email! Try again.");
                                        sleep(2);
                            else:
                                break;
                            break;
                        else:
                            print("Please, you need insert a valid option! Try again.");
                            sleep(2);

                    # update username;
                    while True:
                        os.system("cls");
                        formatFunction("UPDATE USERNAME");
                        print("1 - Yes\n2 - Not");
                        option = str(input("Option: "));
                        if option == "1" or option == "2":
                            if option == "1":

                                while True:
                                    os.system("cls");
                                    formatFunction("UPDATE USERNAME");
                                    newUsername = str(input("Update username: "));
                                    if len(newUsername) == 0:
                                        print("Sorry, you username can not conatin spaces, length less than one character and! Try again.");

                                    if  database.confirmNewUsername(newUsername) == True:
                                        database.updateCustomer.updateCustomerUsername(database.updateCustomer, newUsername, customerUsername);
                                        print("Username confirmed!");
                                        break;
                                    else:
                                        print("Looks like this username is already in use! Try again.");
                                        sleep(2);
                            else:
                                break;
                            break;
                        else:
                            print("Please, you need insert a valid option! Try again.");

                    # update password;
                    while True:
                        os.system("cls");
                        formatMenuFunction("UPDATE PASSWORD");
                        print("1 - Yes\n2 - Not");
                        option = str(input("Option: "));
                        if option == "1" or option == "2":
                            if option == "1":

                                while True:
                                    os.system("cls");
                                    formatFunction("UPDATE PASSWORD");
                                    currentPassword = str(input("Enter current password: "));
                                    if database.findCustomerPasswordFromDatabase(customerUsername, currentPassword) == True:

                                        while True:
                                            os.system("cls");
                                            formatFunction("UPDATE PASSWORD");
                                            newPassword = str(input("Update password: "));
                                            if len(newPassword) >= 10:

                                                confirmNewPassword = str(input("Confirm password: "));
                                                if confirmNewPassword == newPassword:
                                                    database.updateCustomer.updateCustomerPassword(database.updateCustomer, newPassword, customerUsername);
                                                    break;
                                                else:
                                                    print("The password inserted does not correspond to the new password! Try again.");

                                            else:
                                                print("Please, your password needs to have at least 10 characters! Try again.");
                                                sleep(2);
                                    else:
                                        print("Sorry, the password inserted is wrong. Consider review it and try again.");
                                        sleep(2);
                                    break;
                            else:
                                break;
                            break;
                        else:
                            print("Please, you need insert a valid option! Try again.");
                            sleep(2)

                    break;
                else:
                    print("Sorry, it looks like this password does not correspond to the username inserted! Consider review your information and try again.");
                    sleep(2);
            break;
        else:
            print("Sorry, it looks like your username is not in our database! Consider review your information and try again.");
            sleep(2);


def transactionsFunction():
    while True:
        os.system("cls");
        formatFunction("FOR TRANSACTIONS");

        print("1 - Deposit\n2 - Withdraw");
        option = str(input("Option: "));
        if option == "1" or option == "2":
            if option == "1":
                
                while True:
                    os.system("cls");
                    formatFunction("DEPOSIT");
                    accountNumber = str(input("Account number (where the deposit will be executed): "));
                    if database.findAccountNumber(accountNumber) == True:
                        print("Account SUCCESSFULY found!");
                        sleep(3);

                        while True:
                            os.system("cls");
                            formatFunction("MONETARY UNIT")
                            monetaryUnit = str(input("Monetary unit (USD recommended): "));
                            if len(monetaryUnit) > 0:
                                
                                while True:
                                    os.system("cls");
                                    formatFunction("DEPOSIT AMOUNT");
                                    depositAmount = str(input("Deposit amount: "));
                                    if depositAmount > "0":
                                        database.transactions.createDeposit(database.transactions, accountNumber, depositAmount);
                                        break;
                                    else:
                                        print("Please, you need insert a amount before continue! Try again.");
                                        sleep(2)
                                break;
                            else:
                                print("Please, you need insert a monetary unit before continue! Try again.");
                                sleep(2)
                        break;
                    else:
                        print("Sorry, the account number inserted can not be found! Consider review your information and try again!");
                        sleep(2)

            else:
                
                while True:
                    os.system("cls");
                    formatFunction("WITHDRAW");
                    accountNumber = str(input("Account number (where the withdraw will be executed): "));
                    if database.findAccountNumber(accountNumber) == True:
                        print("Account SUCCESSFULY found!");
                        sleep(3);

                        while True:
                            os.system("cls")
                            formatFunction("MONETARY UNIT")
                            monetaryUnit = str(input("Monetary unit (USD recommended): "))
                            if len(monetaryUnit) > 0:

                                while True:
                                    os.system("cls")
                                    formatFunction("WITHDRAW AMOUNT");
                                    withdrawAmount = str(input("Withdraw amount: "));
                                    if withdrawAmount > "0":
                                        database.transactions.createWithdraw(database.transactions, accountNumber, withdrawAmount);
                                        break;
                                    else:
                                        print("Please, you need insert a amount before continue! Try again.");
                                        sleep(2)
                                break;
                            else:
                                print("Please, you need insert a unit before continue! Try again.");
                                sleep(2)

                        break;
                    else:
                        print("Sorry, the account number inserted can not be found! Consider review your information and try again!");
                        sleep(2)
                    
            break;
        else:
            print("Please, you need insert a valid option! Try again.");
            sleep(2);


def checkDetailsFunction():
    os.system("cls");
    formatFunction("CHECK DETAILS");


def removeAccountFunction():
    while True:
        os.system("cls");
        formatFunction("REMOVE ACCOUNT");
        print("1 - Yes\n2 - Not")
        option = str(input("Are you sure? "))
        if option == "1" or option == "2":
            if option == "1":
                while True:
                    os.system("cls");
                    formatFunction("USERNAME")
                    customerUsername = str(input("Username: "));
                    if len(customerUsername) > 0 and database.findCustomerUsernameFromDatabase(customerUsername) == True:

                        while True:
                            os.system("cls");
                            formatFunction("PASSWORD");
                            customerPassword = str(input("Password: "));
                            if len(customerPassword) > 0 and database.findCustomerPasswordFromDatabase(customerUsername, customerPassword) == True:
                                print("Your account will be removed from the system...");
                                sleep(3);
                                
                                while True:

                                    os.system("cls")
                                    formatFunction("ACCOUNT NUMBER")
                                    option = str(input("Do you already have a bank account? [1 - Yes / 2 - Not]: "))
                                    if option == "1":

                                        while True:
                                            os.system("cls")
                                            formatFunction("ACCOUNT NUMBER");
                                            accountNumber = str(input("Account number: "));
                                            if database.findAccountNumber(accountNumber) == True:
                                                if database.removeAccount.removeBankAndAccountFunction(database.removeAccount, accountNumber, customerUsername) == True:
                                                    print("Account SUCCESSFULY removed!");
                                                else:
                                                    print("ERROR trying to remove account! Contact us for possible solutions!");
                                                break;
                                            else:
                                                print("We can not found your account! Try again.");
                                                sleep(3);
                                        break;
                                    else:
                                        if database.removeAccount.removeAccountFunction(database.removeAccount, customerUsername) == True:
                                            print("Account SUCCESSFULY removed!");
                                        else:
                                            print("ERROR trying to remove account! Contact us for possible solutions!");
                                        break;
                            else:
                                if len(customerPassword) == 0:
                                    print("Please, you need insert a password before continue! Try again.");
                                    sleep(2);
                                else:
                                    print("Sorry, the password inserted does not match your username! Consider review your information and try again.")
                                    sleep(2);
                                break;
                            break;
                        break;
                    else:
                        if len(customerUsername) == 0:
                            print("Please, you need insert a username before continue! Try again.");
                            sleep(2);
                        else:
                            print("Sorry, we did not find your username! Consider review your information and try again.");
                            sleep(2);
                
            else:
                break;
            break;
        else:
            print("Please, you need insert a valid option! Try again.");
            sleep(2);


def viewCustomerListFunction():
    os.system("cls");
    formatFunction("CUSTOMER'S LIST");


def exitSystemFunction():
    os.system("cls");
    formatFunction("EXIT SYSTEM");

    while True:
        print("1 - Yes\n2 - Not");
        userOption = str(input("Option: "));
        if userOption == "1" or userOption == "2":
            if userOption == "1":
                break;
            else:
                system.systemFunction();
        else:
            print("Please, you need insert a valid option! Try again.");
