
import os;
import databasepackage;
from system import systemmain;
from datetime import date, datetime;
from time import sleep;
from databasepackage import databaseconnection;
from phone_iso3166.country import phone_country;
import pycountry;

import mysql.connector as mySQL;

# Global variables;
userFullName = ' ';
userBirthday = ' ';
userBirthmonth = ' ';
userBirthyear = ' ';
userBirthDATE = ' ';
userEmailAddress = ' ';
userCountry = ' ';
userCity = ' ';
userPhoneNo = ' ';
userPassport = ' ';
userTicket = ' ';
userAge = 0;

userID = 0;
first_name = ' ';
second_name = ' ';
last_name = ' ';

actual_year = datetime.now().year;

userInformation = [];

conn = mySQL.connect(host="", user="", password="", database="");
cur = conn.cursor();

def exitOrNotFunction():
    # After run the function, the user has the option to continue or exit;
    while True:
        print("1 - Main menu\n2 - Exit")
        opt = str(input("Option: "))
        if (opt == "1" or opt == "2"):
            if (opt == "1"):
                print("Returning to main menu!");
                sleep(3)
                systemmain.system();
            elif (opt == "2"):
                print("Thank you for your presence with us!");
                sleep(3);
                break;
            break;
        else:
            print("Please, you need insert a valid option! Try again.")

def menuOptionsFunction():
    os.system("cls");
    print('\033[1;35;40m\nAIRLINES RESERVATION SYSTEM MENU: ');
    print('1 - Reserve seat');
    print('2 - User ticket');
    print('3 - Flight schedule');
    print('4 - Display passengers');
    print('5 - Flight Details');
    print('6 - Exit system\033[m');

def reserveSeatFunction():
    os.system("cls");
    print('\033[1;33;40m\nRESERVE SEAT MENU:');
    
    # INserting the user ID into the database;
    print('ID');    
    number_of_IDs = 0;
    userID = 0;
    cur.execute("SELECT (user_id) FROM passengers");
    for rows in cur:
        number_of_IDs += 1;
        
    if (number_of_IDs == 0):
        userID = 0;
        print('Your ID: 0');
    else:
        userID = number_of_IDs;
        print("Your ID: ", userID);
    userInformation.append(userID);

    # username confirmation;
    os.system("cls");
    sleep(1)
    print('-'*40);
    print('NAME');
    print('-'*40);
    while True:
        userFullName = str(input('Name: ')).strip().split();

        if (len(userFullName) > 2):
            first_name = userFullName[0].capitalize();
            second_name = userFullName[1].capitalize();
            last_name = userFullName[2].capitalize();
            userInformation.append(first_name);
            userInformation.append(second_name);
            userInformation.append(last_name);
            break;
        else:
            print('Please, you nedd inser a valid username! Try again.');
    
    # user birthdate confirmation;
    os.system("cls");
    sleep(1)
    print("\n", '-'*40);
    print('BIRTHDATE');
    print('-'*40);
    while True:
        # Asking user birthday (DD);
        userBirthday = str(input("DAY (DD): ")).strip();
        if len(userBirthday) == 2:
            if "01" <= userBirthday <= "31":

                while True:
                    # asking user birth month (MM);
                    userBirthmonth = str(input("Month (MM): ")).strip();

                    if len(userBirthmonth) == 2:
                        if "0" <= userBirthmonth <= "12":
                            
                            while True:
                                # Asking user birth year (YYYY);
                                userBirthyear = str(input("Year (YYYY): ")).strip();

                                if len(userBirthyear) == 4:
                                    if userBirthyear < str(actual_year):
                                        DATE = datetime(int(userBirthyear), int(userBirthmonth), int(userBirthday))
                                        # Formating to data before insert into mySQL database;
                                        userBirthDATE = DATE.date().isoformat();
                                        userAge = actual_year - int(userBirthyear);
                                        break;
                                    else:
                                        print("Please, the year inserted is invalid! Try again.")
                                else:
                                    print("Please, the year is invalid! Try again.")
                            break;
                        else:
                            print("Please, the month inserted is invalid! Try again.")
                    else:
                        print("Please, you need insert a month! Try again.")
                break;
            else:
                print("Please, the day inserted is invalid! Try again.")
        else:
            print("Please you need insert a day! Try again.")

    # user email address confirmation;
    os.system("cls");
    sleep(1)
    print("\n", '-'*40);
    print('EMAIL ADDRESS');
    print('-'*40);
    while True:
        userEmailAddress = str(input('Email address: ')).strip();

        if (len(userEmailAddress) != 0 and userEmailAddress.find('@') != -1 and userEmailAddress.find('.') != -1):
            userInformation.append(userEmailAddress);
            break;
        else:
            print("Please, you need insert a valid email address! Try again.")

     # user phone number confirmation;
    os.system("cls");
    sleep(1)
    print("\n", '-'*40);
    print('PHONE');
    print('-'*40);
    while True:
        userPhoneNo = str(input('Phone: '));

        if (len(userPhoneNo) != 0):
            userPhoneNo = "+" + userPhoneNo;

            # checking user country since phone number inseted;
            country = pycountry.countries.get(alpha_2=phone_country(userPhoneNo));
            userCountry = country.name;
            userOfficialCountryName = country.official_name;
            break;
        else:
            print('Please, you need insert a phone number valid! Try again.');

    # user country confirmation;
    '''os.system("cls");
    sleep(1)
    print("\n", '-'*40);
    print('COUNTRY');
    print('-'*40);
    while True:
        userCountry = str(input('Country: ')).upper().strip().capitalize();
        
        if (len(userCountry) != 0):
            userInformation.append(userCountry);
            break;
        else:
            print('Please, you need insert a country valid! Try again.');'''
        
    # user city confirmation;
    os.system("cls");
    sleep(1)
    print("\n", '-'*40);
    print('CITY')
    print('-'*40)
    while True:
        userCity = str(input('City: ')).upper().strip().capitalize();
        
        if (len(userCity) != 0):
            userInformation.append(userCity);
            break;
        else:
            print('Please, you need insert a valid city! Try again.');

    # user passport confirmation;
    os.system("cls");
    sleep(1)
    print("\n", '-'*40);
    print('PASSPORT');
    print('-'*40);
    while True:
        userPassport = str(input('Passport: '))

        if (len(userPassport) != 0):
            userInformation.append(userPassport);
            break;
        else:
            print('Please, you need insert a passport number valid! Try again.');

    # user ticket confirmation;
    os.system("cls");
    sleep(1);
    print("\n", '-'*40);
    print('TICKET');
    print('-'*40);
    while True:
        userTicket = str(input('Ticket: '))
        
        if (len(userTicket) != 0):
            userInformation.append(userTicket);
            break;
        else:
            print('Please, you need insert a ticket number valid! Try again.');

    os.system("cls");
    print("INSERTING USER TO DATABASE")
    print('-\033[m'*30)
    # Function inside the database package where the user will be inserted into the database;
    databaseconnection.insertUserToDatabase(userID, first_name, second_name, last_name, userAge, userBirthDATE, userEmailAddress, userOfficialCountryName, userCountry, userCity, userPhoneNo, userPassport, userTicket);

'''def showUserInformation():
    print(userInformation);
    for i in userInformation:
        print(type(i));
'''

def userTicketFunction():
    os.system("cls");
    print('USER TICKET MENU')

    while True:
        userFullName = str(input("Full name: ")).strip().split()
        if (len(userFullName) > 2):
            while True:
                os.system("cls");
                userID = int(input("Insert your ID: "));
                if (len(str(userID)) != 0):
                    os.system("cls");
                    print("SEARCHING USER TICKET");
                    sleep(3);
                    databaseconnection.getUserTicketDatabase(userID, userFullName[0], userFullName[1], userFullName[2]);
                    exitOrNotFunction();

                    break;
                else:
                    print("You need insert a valid ID! Try again.");
                break;
        else:
            print("You need insert a valid name! Try again.");
        break;

def flightScheduleFunction():
    os.system("cls");
    print('\033[1;36;40m\nFLIGHT SCHEDULE MENU: \033[m')

    flight_number = 0;
    while True:
        flight_number = int(input("Flight number (NNNN): "));
        if len(str(flight_number)) == 4:
            databaseconnection.getFlightSchedule(flight_number)
            # After run the function, the user has the option to continue or exit;
            while True:
                print("1 - Main menu\n2 - Exit")
                opt = str(input("Option: "))
                if (opt == "1" or opt == "2"):
                    if (opt == "1"):
                        print("Returning to main menu!");
                        sleep(3)
                        systemmain.system();
                    elif (opt == "2"):
                        print("Thank you for your presence with us!");
                        sleep(3);
                        break;
                    break;
                else:
                    print("Please, you need insert a valid option! Try again.")
            break;
        else:
            print("Please, you need insert a valid flight number! Try again.")


def displayPassengersFunction():
    os.system("cls")
    print('DISPLAY PASSENGER MENU')

    while True:
        userID = int(input("Insert user ID: "))
        if (len(str(userID)) != 0):
            databaseconnection.displayUserFromDatabase(userID);
            exitOrNotFunction()
            break;
        else:
            print("Please, you need insert a valid ID! Try again.")

class flightFunctions:

    # Global flightFunctions variables;
    flight_ID = ' ';
    flightNumber = ' ';
    flightName = ' ';
    flightOrigin = ' ';
    flightDestination = ' ';
    flightTime = ' ';
    flightDepartureTime = ' ';
    flightArrivalTime = ' ';
    flightAmount = ' ';
    flightAvailability = ' ';

    def addNewFlight():
        print('\033[1;33mADD NEW FLIGHT')

        sleep(1)
        print('-'*40);
        print("FLIGHT NUMBER")
        print('-'*40);
        while True:
            flightNumber = str(input("Flight number: "));
            if (len(flightNumber) != 0):

                sleep(1)
                print('-'*40);
                print("FLIGHT NAME")
                print('-'*40);
                while True:
                    flightName = str(input("Flight name: "));
                    if (len(flightName) != 0):

                        sleep(1)
                        print('-'*40);
                        print("FLIGHT ORIGIN")
                        print('-'*40);
                        while True:
                            flightOrigin = str(input("Flight origin: "));
                            if len(flightOrigin) != 0:

                                sleep(1)
                                print('-'*40);
                                print("FLIGHT DESTINATION")
                                print('-'*40);
                                while True:
                                    flightDestination = str(input("Flight destination: "));
                                    if (len(flightDestination) != 0):

                                        sleep(1)
                                        print('-'*40);
                                        print("FLIGHT DEPARTURE TIME")
                                        print('-'*40);
                                        while True:
                                            flightDepartureTime = str(input("Flight departure time (YYYY-MM-DD): "));
                                            if len(flightDepartureTime) != 0:

                                                sleep(1);
                                                print("-"*40);
                                                print("FLIGHT ARRIVAL TIME")
                                                print("-"*40)
                                                while True:
                                                    flightArrivalTime = str(input("Flight arrival time (YYYY-MM-DD): "))
                                                    if len(flightArrivalTime) != 0:

                                                        print("-"*40)
                                                        print("FLIGHT TIME")
                                                        print("-"*40)
                                                        while True:
                                                            flightTime = str(input("Flight time: "))
                                                            if len(flightTime) != 0:

                                                                sleep(1)
                                                                print('-'*40);
                                                                print("FLIGHT AMOUNT")
                                                                print('-'*40);
                                                                while True:
                                                                    flightAmount = str(input("Flight amount: "))
                                                                    if len(flightAmount) != 0:

                                                                        sleep(1)
                                                                        print('-'*40);
                                                                        print("FLIGHT AVAILABILITY")
                                                                        print('-'*40);
                                                                        while True:
                                                                            print("1 - Available\n2 - Not Available")
                                                                            flightAvailability = str(input("Flight availability: ")).upper()
                                                                            if len(flightAvailability) != 0:
                                                                                if flightAvailability == "1":
                                                                                    flightAvailability = "A";
                                                                                elif flightAvailability == "2":
                                                                                    flightAvailability = "U";
                                                                                print("INSERTING FLIGHT TO DATABASE")
                                                                                print('-\033[m'*30)
                                                                                exitOrNotFunction()
                                                                            
                                                                                break;
                                                                            else:
                                                                                print("Please, you need insert a valid flight availability. Try again.")

                                                                        break;
                                                                    else:
                                                                        print("Please, you need insert a valid flight amount. Try again.")

                                                                break;
                                                            else:
                                                                print("Please, you need insert a valid time. Try again.")

                                                        break;
                                                    else:
                                                        print("Please, you need insert a valid flight arrival time. Try again.")

                                                break;
                                            else:
                                                print("Please, you need insert a valid flight time. Try again.");

                                        break;
                                    else:
                                        print("Please, you need insert a valid flight destination. Try again.")

                                break;
                            else:
                                print("Please, you need insert a valid flight origin. Try again.")

                        break;
                    else:
                        print("Please, you need insert a valid flight name! Try again.")

                break;
            else:
                print("Please, you need insert a valid flight number! Try again.\033[m")

        # Calculating flight time in hours throughout the distance bewteen the origin and the destination;

        # Calculating flight ID throughout the previews data inserted into the database;
        number_of_IDs = 0;
        cur.execute("SELECT flight_id FROM flight_details")
        for row in cur:
            number_of_IDs += 1;
        flight_ID = number_of_IDs;

        # Inserting the data insde the function located inside the database package;
        databaseconnection.addFlightDatabase(flight_ID, flightNumber, flightName, flightOrigin, flightDestination, flightDepartureTime, flightArrivalTime, flightTime, flightAmount, flightAvailability);

    def editFlight():
        print('\033[1;33m\nEDIT FLIGHT')

        number_of_flight_IDs = 0;

        while True:
            flight_ID = str(input("Flight ID: "));
            if (len(flight_ID) != 0):

                # edit flight number;
                while True:
                    print("-"*40)
                    print("1 - Change\n2 - Not change");
                    option = str(input("Edit flight number? "));
                    if (option == "1" or option == "2"):
                        if (option == "1"):
                            while True:
                                new_flight_number = str(input("New flight Number: "));
                                if len(new_flight_number) != 0:
                                    databaseconnection.flightClass.newFlightNumber(flight_ID, int(new_flight_number));
                                    exitOrNotFunction()

                                    break;
                                else:
                                    print("Please you need insert a flight number! Try again.");
                        else:
                            break;

                        break;
                    else:
                        print("Please you need insert a valid option! Try again.");

                # edit flight name;
                while True:
                    print("-"*40);
                    print("1 - Change\n2 - Not change");
                    option = str(input("Edit flight name? "));
                    if (option == "1" or option == "2"):
                        if (option == "1"):
                            while True:
                                new_flight_name = str(input("New flight name: "));
                                if len(new_flight_name) != 0:
                                    databaseconnection.flightClass.newFlightName(flight_ID, new_flight_name);
                                    exitOrNotFunction()

                                    break;
                                else:
                                    print("Please you need insert a flight number! Try again.");
                        else:
                            break;

                        break;
                    else:
                        print("Please, you need insert a valid option! Try again.")

                # edit flight origin;
                while True:
                    print("-"*40);
                    print("1 - Change\n2 - Not change");
                    option = str(input("Edit flight origin? "));
                    if (option == "1" or option == "2"):
                        if (option == "1"):
                            while True:
                                new_flight_origin = str(input("New flight origin: "));
                                if len(new_flight_origin) != 0:
                                    databaseconnection.flightClass.newFlightOrigin(flight_ID, new_flight_origin);
                                    exitOrNotFunction()

                                    break;
                                else:
                                    print("Please, you need insert a flight origin! Try again.")
                        else:
                            break;
                        break;
                    else:
                        print("Please, you need insert a valid option! Try again.")

                # edit flight destination;
                while True:
                    print("-"*40);
                    print("1 - Change\n2 - Not change");
                    option = str(input("Edit flight destination? "));
                    if (option == "1" or option == "2"):
                        if (option == "1"):
                            while True:
                                new_flight_destination = str(input("New flight destination: "));
                                if len(new_flight_destination) != 0:
                                    databaseconnection.flightClass.newFlightDestination(flight_ID, new_flight_destination);
                                    exitOrNotFunction()

                                    break;
                                else:
                                    print("Please, you need insert a flight destination! Try again.")
                        else:
                            break;
                        break;
                    else:
                        print("Please, you need insert a valid option! Try again.")
                
                # edit flight time
                while True:
                    print("-"*40);
                    print("1 - Change\n2 - Not change");
                    option = str(input("Edit flight time? "));
                    if (option == "1" or option == "2"):
                        if (option == "1"):
                            while True:
                                new_flight_time = str(input("New flight time: "));
                                if len(new_flight_time) != 0:
                                    databaseconnection.flightClass.newFlightTime(flight_ID, new_flight_time);
                                    exitOrNotFunction()

                                    break;
                                else:
                                    print("Please, you need insert a flight time! Try again.")
                        else:
                            break;
                        break;
                    else:
                        print("Please, you need insert a valid option! Try again.")

                # edit flight amount;
                while True:
                    print("-"*40);
                    print("1 - Change\n2 - Not change");
                    option = str(input("Edit flight amount? "));
                    if (option == "1" or option == "2"):
                        if (option == "1"):
                            while True:
                                new_flight_amount = str(input("New flight amount: "));
                                if len(new_flight_amount) != 0:
                                    databaseconnection.flightClass.newFlightAmount(flight_ID, new_flight_amount);
                                    exitOrNotFunction()

                                    break;
                                else:
                                    print("Please, you need insert a valid flight amount! Try again.");
                            break;
                        else:   
                            break;
                    else:
                        print("Please, you need insert a valid option! Try again.");

                break;
            else:
                print("Please insert a valid ID.");

        exitOrNotFunction()
    
    def deleteFlight():
        print('\033[1;33mDELETE FLIGHT')

        while True:
            flight_ID = str(input("Flight ID: "));
            if len(flight_ID) != 0:
                databaseconnection.flightClass.deleteFlightFromDatabase(flight_ID);
                exitOrNotFunction()

                break;
            else:
                print("Please, you need insert a flight ID! Try again.\033[m");

    def flightDepartureAndArrive():
        print("\033[1;33mFLIGHT DEPARTURE AND ARRIVE")

        while True:
            flight_ID = str(input("Flight ID: "));
            if len(flight_ID) != 0:
                databaseconnection.flightClass.searchDpartureAndArrivalInDatabase(flight_ID);
                exitOrNotFunction()

                break;
            else:
                print("Please, you need insert a flight ID! Try again.\033[m");

def flightDetailsFunction():
    os.system("cls")
    print('FLIGHT DETAILS MENU')

    print("\033[1;35m1 - Add flight")
    print("2 - Edit flight")
    print("3 - Delete flight")
    print("4 - Flight leave and arrive")
    print("5 - Main menu")
    print("6 - Exit system\033[m")

    while True:
        userOption = str(input("Option: "))
        if ("6" < userOption < "1"):
            print("Please, you need insert a valid option! Try again.")
        else:
            if (userOption == "1"):
                flightFunctions.addNewFlight();
                break;

            elif (userOption == "2"):
                flightFunctions.editFlight();
                break;
            
            elif (userOption == "3"):
                flightFunctions.deleteFlight();
                break;
            
            elif (userOption == "4"):
                flightFunctions.flightDepartureAndArrive();
                break;
            
            elif (userOption == "5"):
                systemmain.system();
            
            else:
                exitOrNotFunction()
                break;

def exitSystemFunction():
    os.system("cls")
    while True:
        print("EXIT")
        print('Are you sure? ')
        print('1 - Yes')
        print('2 - Not')
        userExitOption = str(input('Option: '))
        if ("1" <= userExitOption <= "2"):
            if (userExitOption == "1"):
                print("Thank you for your presence with us!")
                break;
            else:
                systemmain.system();
            break;
        else:
            print("Please, you need insert a valid option! Try again.")
