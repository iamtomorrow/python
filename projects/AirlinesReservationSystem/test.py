from time import sleep
from typing import Container, Mapping
# from databasepackage import databaseconnection
import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
# from functionspackage import functions
from phone_iso3166.country import phone_country
import pycountry


germany = pycountry.countries.get(alpha_2='US');
print(germany.name);
print(germany.numeric)


'''country = str(input("Country: "))

def searchCodeCountry(countryName):
    try:
        result = pycountry.countries.search_fuzzy(countryName)
        return result[0].alpha_3
    except Exception as exc:
        return exc

print(searchCodeCountry(country))'''


'''userId = 3
databaseconnection.insertUserID(userId);
'''host = "",
    user = "",
    password = "",
    database = ""
'''

cur = conn.cursor();

# Here, I'm trying to get the number of employees (rows) inside the table before insert a new employee. After this, Python will can generate a new ID;
numberOfID = 0;
cur.execute("SELECT (emp_id) FROM employee")
for a in cur:
    numberOfID += 1;

cur.execute("SELECT * FROM employee");
for i in cur:
    print(i)

print('The number os rows is equal to ', numberOfID);
'''
'''# Getting country code by request;

url = "https://www.countrycode.org"

webpage = requests.get(url)

webpage_soup = BeautifulSoup(webpage.text, 'html.parser')

all_class = webpage_soup.findAll('h2', {'class':'text-center'})

for span in all_class:
    print(span)
'''

'''try:
    open('countrycode.txt')
    print('The document is open now!')
except:
    print('ERROR! The document cannnot be open.')

text = str(input('Country: '))

file = open('countrycode.txt', 'a')
file.write(text)

'''

'''now = datetime.today()

print(now)
print(now.year)
print(now.month)
print(now.day)

birthday = '2001-06=13';
yearBirth = int(birthday[0:4]);
print(yearBirth)

print(type(yearBirth))
print(type(birthday))
'''

'''full_name = "Talisson Rodrigues Pinho";

print(full_name.split());
print(len(full_name.split()));
print(full_name.split()[0]);
'''

'''while True:
    userBirthday = str(input('Birthday (YYYY-MM-DD): '));

    if (len(userBirthday) == 10):
        userYearBirthday = int(userBirthday[0:4]);
        userMonthBirthday = int(userBirthday[5:7]);
        userDayBirthday = int(userBirthday[8:]);
        now = datetime.today();
        userAge = now.year - userYearBirthday;
        
        if (userMonthBirthday > now.month or userDayBirthday > now.day):
            userAge +- 1;
        else:
            userAge = userAge;
            print('DATE CONFIRMED!')
            print('-'*30)
        break;
    else:
        print('Please, you need insert a date valid! Try again.')

print(userBirthday.find('-')) # Output = -1 if there's no '-' in the birthday;
'''

'''birth_day = str(input("Day: ")).strip()
birth_month = str(input("Month: ")).strip()
birth_year = str(input("Year: ")).strip()

birth_date = (f'{birth_year}-{birth_month}-{birth_day}')
print(birth_date)
print(type(birth_date))

birth_date_date = datetime(int(birth_year), int(birth_month), int(birth_day))
birthDate = birth_date_date.date()
print(birthDate)
'''

'''userBirthday = ' ';
userBirthmonth = ' ';
userBirthyear = ' ';

print("BIRTHDATE")

while True:
    userBirthday = str(input("DAY (DD): "))

    if len(userBirthday) == 2:
        if "01" <= userBirthday <= "31":
            print("Ok")
            break;
        else:
            print("Please, the day is invalid! Try again.")
    else:
        print("Please you need insert a day! Try again.")
    
print("Yeahhhh")
'''

'''actual_year = datetime.now().year

print(actual_year)
print(type(actual_year))
print(type(str(actual_year)))
'''

'''while True:
    print("TEST")
    amount = str(input("Amount: "));
    if len(amount) != 0:
        print("Yeahhhh");
        sleep(1)
        while True:
            country = str(input("Country: "));
            if len(country) != 0:
                print("Yeahhhh");
                sleep(1);
                break;
            else:
                print("Try again.")
        break;
    else:
        print("Try again!");
'''

'''class parentClass:
    def __init__(self, username, userbirthdate):
        self.username = username;
        self.userbirthdate = userbirthdate;

    def addNewFlight(self):
        print("ADD NEW FLIGHT");
        print(self.username);


obj = parentClass("Talisson", "2001");
obj.addNewFlight();
'''
'''new_flight_number = ' ';
new_flight_name = ' ';

while True:
    print("1 - Change\n2 - Not change")
    option = str(input("Edit flight number: "))
    if (option == "1" or option == "2"):
        if (option == "1"):
            while True:
                new_flight_number = str(input("New flight number: "));
                if len(new_flight_number) != 0:
                    print("ok");
                    break;
                else:
                    print("Try again!")
            break;
        else:
            break;
    else:
        print("Please, you need insert a valid option! Try again.");

while True:
    print("1 - Change\n2 - Not change")
    option = str(input("Edit flight name: "))
    if (option == "1" or option == "2"):
        if (option == "1"):
            while True:
                new_flight_name = str(input("New flight name: "));
                if len(new_flight_name) != 0:
                    print("ok");
                    break;
                else:
                    print("Try again!")
            break;
        else:
            break;
    else:
        print("Please, you need insert a valid option! Try again.");
        '''
