# DATABASE connection

import os;
from os import replace;
from system import systemmain;
from time import sleep;
import mysql.connector as SQLConn;
# from functionspackage import functions


'''conn = SQLConn.connect(
    host = "",
    user = "",
    password = "",
    database = ""
)
cur = conn.cursor()'''

def insertUserToDatabase(user_id, first_name, second_name, last_name, age, birthday, email_address, country_official_name, country, city, phone, passport, ticket):
    os.system("cls");
    sleep(1);
    print('\033[1;33;40m')
    print("-"*40)
    print("INFORMATIONS")
    print("-"*40)
    print("ID: ", user_id)
    sleep(0.5)
    print("Name: ", first_name, " ", second_name, " ", last_name)
    sleep(0.5)
    print("Age: ", age)
    sleep(0.5)
    print("Birthdate: ", birthday)
    sleep(0.5)
    print("Email address: ", email_address)
    sleep(0.5)
    print("Country: ", country)
    sleep(0.5)
    print("Country Official Name: ", country_official_name);
    sleep(0.5)
    print("CIty: ", city)
    sleep(0.5)
    print("Phone: ", phone)
    sleep(0.5)
    print("Passport: ", passport)
    sleep(0.5)
    print(f"Ticket: {ticket} \033[m")
    sleep(0.5)
    print("-"*40)
    print("ACCESSING DATABASE")
    conn = SQLConn.connect(
        host = "",
        user = "",
        password = "",
        database = ""
    )
    cur = conn.cursor()
    sleep(3);

    sql = "INSERT INTO passengers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        cur.execute(sql, (user_id, first_name, second_name, last_name, age, birthday, email_address, country, city, phone, passport, ticket));
        conn.commit();
        conn.close();
        print("\n", "-"*40);
        print("\033[1;32mSUCCESSFUL REGISTRATION!\033[m");
        print("-"*40);
        sleep(3);
        while True:
            os.system("cls");
            sleep(0.5);
            print("1 - Exit\n2 - Main menu")
            opt = str(input("Option: "))
            if (opt == "1"):
                conn.close()
                print("\033[1;36mThank you for your presence!\033[m")
                break;
            elif (opt == "2"):
                systemmain.system();
            else:
                print("Please, you need insert a valid option! Try again.");

    except Exception as exc:
        print("\n", "-"*40);
        print("\033[1;31mERROR in the registration process!\033[m");
        print("-"*40);
        print(exc)
        conn.close();
        print("\nThe system will reset!");

def getUserTicketDatabase(user_id, first_name, second_name, last_name):
    print("ACCESSING DATABASE")
    conn = SQLConn.connect(
        host = "",
        user = "",
        password = "",
        database = ""
    )
    cur = conn.cursor()
    sleep(3);

    try:
        print("USER TICKET")
        cur.execute("SELECT ticket FROM passengers WHERE user_id LIKE {}".format(user_id))
        print("Name: ", first_name, " ", second_name, " ", last_name)
        for row in cur:
            print(f'Ticket: {row}')
        conn.close();
    except Exception as exc:
        print(exc);
        conn.close();

def getFlightSchedule(flightNumber):
    print("ACCESSING DATABASE")
    conn = SQLConn.connect(
        host = "",
        user = "",
        password = "",
        database = ""
    )
    cur = conn.cursor()
    sleep(3);

    try:
        cur.execute(f"SELECT * FROM flight_schedule WHERE flight_number = {flightNumber}")
        print("-"*50);
        for row in cur:
            for i in range(0, 7):
                if i == 0:
                    print(f"\033[1;36m\nFLIGHT ID:......................{row[0]}");
                    print("-"*50);
                elif i == 1:
                    print(f"FLIGHT NUMBER:..................{row[1]}");
                    print("-"*50);
                elif i == 2:
                    print(f"ORIGIN:.........................{row[2]}");
                    print("-"*50);
                elif i == 3:
                    print(f"DESTINATION:....................{row[3]}");
                    print("-"*50);
                elif i == 4:
                    print(f"DEPARTURE:......................{row[4]}");
                    print("-"*50);
                elif i == 5:
                    print(f"ARRIVAL:........................{row[5]}")
                    print("-"*50);
                elif i == 6:
                    print(f"AIRCRAFT:.......................{row[6]}\033[m");
                    print("-"*50);
    except Exception as exc:
        print("ERROR trying to find flight schedule!");
        print(exc);
        conn.close();

def displayUserFromDatabase(ID):
    print("ACCESSING DATABASE")
    conn = SQLConn.connect(
        host = "",
        user = "",
        password = "",
        database = ""
    )
    cur = conn.cursor()
    sleep(3);

    try:
        sql = "SELECT * FROM passengers WHERE user_id = '(%s)'";
        value = (ID);
        cur.execute(sql, value);
        conn.commit();
        print("-"*40)
        print("PASSENGER");
        print("-"*40)
        for row in cur:
            print(row);

        conn.close();
    except Exception as exc:
        print("\033[1;32mERROR trying to find your informations!\033[m")
        print(exc)
        conn.close();

def addFlightDatabase(flight_id, flight_number, flight_name, flight_origin, flight_destination, flight_departure_time, flight_arrival_time, flight_time, flight_amount, flight_availability):
    sleep(3);
    print("\033[1;33m-"*40)
    print("INFORMATIONS")
    print("-"*40)
    print("Flight ID: ", flight_id);
    sleep(0.5);
    print("Flight number: ", flight_number);
    sleep(0.5)
    print("Flight name: ", flight_name);
    sleep(0.5);
    print("Flight origin: ", flight_origin);
    sleep(0.5);
    print("Flight destination: ", flight_destination);
    sleep(0.5);
    print("Flight time: ", flight_time);
    sleep(0.5);
    print("Departure time: ", flight_departure_time);
    sleep(0.5);
    print("Arrival time: ", flight_arrival_time);
    sleep(0.5);
    print("Flight amount: ", flight_amount);
    sleep(0.5);
    print(f"Flight Availabilty: {flight_availability}\033[m");
    sleep(0.5);
    print("ACCESSING DATABASE");
    conn = SQLConn.connect(
        host = "",
        user = "",
        password = "",
        database = ""
    )
    cur = conn.cursor()
    sleep(3);

    sql = "INSERT INTO flight_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)";
    try:
        cur.execute(sql, (flight_id, flight_number, flight_name, flight_origin, flight_destination, flight_departure_time, flight_arrival_time, flight_time, flight_amount, flight_availability));
        conn.commit();
        print("\n", '\033[1;32m',  "-"*40);
        print("SUCCESSFUL FLIGHT ADDED!\033[m");
        print('\033[1;32m', "-"*40);
        while True:
            sleep(0.5)
            print("1 - Exit\n2 - Main menu")
            opt = str(input("Option: "))
            if (opt == "1"):
                conn.close()
                print("\033[1;36mThank you for your presence!\033[m")
                break;
            elif (opt == "2"):
                systemmain.system();
            else:
                print("Please, you need insert a valid option! Try again.");

    except Exception as exc:
        print("\n", "-"*40);
        print("\033[1;31mERROR trying to add new flight process!\033[m");
        print("-"*40);
        print(exc);
        conn.close();
        print("\nThe system will reset!")

class flightClass():

    new_flight_number = ' ';
    new_flight_name = ' ';
    new_flight_origin = ' ';
    new_flight_destination = ' ';
    new_flight_departure_time = ' '; 
    new_flight_arrival_time = ' ';
    new_flight_time = ' ';
    new_flight_amount = ' ';
    new_flight_availability = ' ';
    

    # edit flight number; 
    def newFlightNumber(ID, new_flight_number):
        print("\nACCESSING DATABASE");
        conn = SQLConn.connect(
            host = "",
            user = "",
            password = "",
            database = ""
        )
        cur = conn.cursor()
        sleep(3);
        try: 
            sql = "UPDATE flight_details SET flight_number = '%s' WHERE flight_id = (%s)";
            values = (new_flight_number, int(ID));
            cur.execute(sql, values);
            conn.commit();

            print("\n", '\033[1;32m',  "-"*40);
            print("SUCCESSFUL! The flight number was updated!\033[m");
            print("-"*40);
        except Exception as exc:
            print("ERROR trying to update flight number!");
            print(exc);
            conn.close();

    def newFlightName(ID, new_flight_name):
        print("\nACCESSING DATABASE");
        conn = SQLConn.connect(
            host = "",
            user = "",
            password = "",
            database = ""
        )
        cur = conn.cursor()
        sleep(3);
        try:
            cur.execute(f"UPDATE flight_details SET flight_name = '{new_flight_name}' WHERE flight_id = {ID}");
            conn.commit();
            print('\033[1;32m',  "-"*40);
            print("SUCCESSFUL! The flight name was updated!\033[m");
            print('\033[1;32m', "-"*40);
        except Exception as exc:
            print("ERROR trying to update flight name!");
            print(exc);
            conn.close();

    def newFlightOrigin(ID, new_flight_origin):
        print("\nACCESSING DATABASE");
        conn = SQLConn.connect(
            host = "",
            user = "",
            password = "",
            database = ""
        )
        cur = conn.cursor()
        sleep(3);
        try:
            cur.execute(f"UPDATE flight_details SET flight_origin = '{new_flight_origin}' WHERE flight_id = {ID}");
            conn.commit();
            print('\033[1;32m',  "-"*40);
            print("SUCCESSFUL! The flight origin was updated!\033[m");
            print('\033[1;32m', "-"*40);
        except Exception as exc:
            print("ERROR trying to update flight origin!");
            print(exc);
            conn.close();

    def newFlightDestination(ID, new_flight_destination):
        print("\nACCESSING DATABASE");
        conn = SQLConn.connect(
            host = "",
            user = "",
            password = "",
            database = ""
        )
        cur = conn.cursor()
        sleep(3);
        try:
            cur.execute(f"UPDATE flight_details SET flight_destination = '{new_flight_destination}' WHERE flight_id = {ID}");
            conn.commit();
            print('\033[1;32m',  "-"*40);
            print("SUCCESSFUL! The flight destination was updated!\033[m");
            print('\033[1;32m', "-"*40);
        except Exception as exc:
            print("ERROR trying to update flight destination!");
            print(exc);
            conn.close();

    def newFlightTime(ID, new_flight_time):
        print("\nACCESSING DATABASE");
        conn = SQLConn.connect(
            host = "",
            user = "",
            password = "",
            database = ""
        )
        cur = conn.cursor()
        sleep(3);
        try:
            cur.execute(f"UPDATE flight_details SET flight_time = '{new_flight_time}' WHERE flight_id = {ID}");
            conn.commit();
            print('\033[1;32m',  "-"*40);
            print("SUCCESSFUL! The flight time was updated!\033[m");
            print('\033[1;32m', "-"*40);
        except Exception as exc:
            print("ERROR trying to update flight time!");
            print(exc);
            conn.close();

    def newFlightAmount(ID, new_flight_amount):
        print("\nACCESSING DATABASE");
        conn = SQLConn.connect(
            host = "",
            user = "",
            password = "",
            database = ""
        )
        cur = conn.cursor()
        sleep(3);
        try:
            cur.execute(f"UPDATE flight_details SET flight_amount = '{new_flight_amount}' WHERE flight_id = {ID}");
            conn.commit();
            print('\033[1;32m',  "-"*40);
            print("SUCCESSFUL! The flight amount was updated!\033[m");
            print('\033[1;32m', "-"*40);
        except Exception as exc:
            print("ERROR trying to update flight amount!");
            print(exc);
            conn.close();

    def deleteFlightFromDatabase(ID):
        print("ACCESSING DATABASE")
        conn = SQLConn.connect(
            host = "",
        user = "",
        password = "",
        database = ""
        )
        cur = conn.cursor()
        sleep(3);
        
        print("\n")
        print("Searching flight ID...");
        sleep(3);

        try:
            sql = "SELECT * FROM flight_details WHERE flight_id = '(%s)'";
            value = (ID);
            cur.execute(sql, value);
            print("\033[1;32mThe flight was found!\033[m");
            print("\033[1;33m-"*40);
            print(f"FLIGHT ID {ID}\033[m");

            for row in cur:
                print(row);

            while True:
                print("\n")
                print("This flight will be deleted! Continue?\n1 - Yes\n2 - Not")
                opt = str(input("Option: "))
                if opt == "1" or opt == "2":
                    if opt == "1":
                        print("\n", "-"*40);
                        print("DELETING FLIGHT");
                        print("-"*40);
                        sleep(1);
                        
                        try:
                            sql = "DELETE FROM flight_details WHERE flight_id = '(%s)'";
                            value = (ID);
                            cur.execute(sql, value);
                            conn.commit();

                            print("\n", '\033[1;32m',  "-"*40);
                            print("\033[1;32mFLIGHT SECCESSFULY DELETED\033[m");
                            print("\n", '\033[1;32m',  "-"*40);

                            conn.close();

                        except Exception as exc:
                            print("\033[1;31mERROR trying to delete the flight!\033[m");
                            print(exc);
                            conn.close();
                        break;
                    else:
                        print("\n", "-"*40);
                        print("DELETE FLIGHT ABOART");
                        print("\n", "-"*40);
                        conn.close();
                        sleep(1);
                        systemmain.system();
                    break;
                else:  
                    print("Please, you need insert a valid option! Try again.");

        except Exception as exc:
            print("\033[1;31mERROR searching the flight! Maybe the flight does not exist!\033[m")
            print(exc);
            conn.close();

    def searchDpartureAndArrivalInDatabase(ID):
        print("ACCESSING DATABASE")
        conn = SQLConn.connect(
            host = "",
            user = "",
            password = "",
            database = ""
        )
        cur = conn.cursor()
        sleep(3);

        print("\n")
        print("Searching flight Departure and Arrival...");
        sleep(3);

        try:
            sql = "SELECT departure_date_time, arrival_date_time FROM flight_details WHERE flight_id = '(%s)'";
            value = (ID);
            cur.execute(sql, value);
            conn.commit();
            for row in cur:
                print(row);

            conn.close();
        except Exception as exc:
            print("ERROR searching the flight!");
            print(exc);
            conn.close();
