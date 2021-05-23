
# from functions import createAccountFunction
# import database
from time import sleep
from datetime import date, datetime, timezone;
import psycopg2

class classConnection:
    try:
        connection = psycopg2.connect(user="postgres",
                                            port = "5432",
                                            password="Tomorrowuser2021",
                                            database="BankManagementDatabase");
        cur = connection.cursor();
    except Exception as exc:
        print(exc);

class getLastID(classConnection):
    
    def __init__(self):
        super().__init__()

    def lastID(self):
        try:
            query = "SELECT customer_id FROM customers ORDER BY customer_id DESC LIMIT 1";
            self.cur.execute(query)
            rows = self.cur.fetchall();
            for row in rows:
                return row[0] + 1;
        except Exception as exc:
            print(exc)
            return -1;

userID = getLastID.lastID(classConnection);
print(userID);
print(type(userID))

print("FINISH");

'''year = datetime.now().year;
print(type(year))'''

# year = str(input("Enter Year: "));
year = 2001;
# month = str(input("Enter Month: "));
month = 12;
# day = str(input("Enter Day: "))
day = 12;

'''DATE = datetime(int(year), int(month), int(day))
realDATE = DATE.date().isoformat()
print(realDATE)
print(type(realDATE))'''

'''birthdate = datetime(2001, 6, 13)
custBirthDate = birthdate.replace(tzinfo=timezone.utc).timestamp();
print(custBirthDate)
print(type(custBirthDate))
'''

'''try:
    connection = psycopg2.connect(user = "postgres",
                                password = "Tomorrowuser2021",
                                host = "localhost",
                                port = "5432",
                                database = "testingDataPostgreSQL")
    cur = connection.cursor();
    print("Connected!");
    sleep(2)

    try:
        cur.execute(f"INSERT INTO dateTable (date_id, current_date) VALUES ({0}, {'2001-06-13'})")
        print("Data inserted!")
    except Exception as exc:
        print(exc)

except Exception as exc:
    print(exc)


finally:
    if connection:
        cur.close()
        connection.close()'''