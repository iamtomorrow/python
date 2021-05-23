
from time import sleep;
import os;
import psycopg2;

# PostgreSQL database connection;
class databaseConnection:
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "password",
                                      host = "localhost",
                                      port = "5432",
                                      database = "databasename");
        cur = connection.cursor();
    except Exception  as exc:
        print(exc);


# function created to
def getNewCustomerID():
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "password",
                                      host = "localhost",
                                      port = "5432",
                                      database = "databasename");
        cur = connection.cursor();

        query = "SELECT customer_id FROM customers ORDER BY customer_id DESC LIMIT 1";
        cur.execute(query);
        rows = cur.fetchall();
        nextID = 1;
        for row in rows:
            lastID = row[0];

        nextID += lastID;
        return nextID;
        
    except Exception as exc:
        print(exc);
        return -1;

    finally:
        if connection:
            connection.close();
            cur.close();

def insertCustomerToDatabase(customerID, customerStName, customerNdName, customerLastName, customerBirthdate, customerCountry, customerCity, customerPhone, customerEmail, customerAge, dateBecomeCustomer, customerCitizenNumber, customerUsername, customerPassword):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "password",
                                      host = "localhost",
                                      port = "5432",
                                      database = "databasename");
        cur = connection.cursor();

        # here, the function will execute the main propose of it;
        query = f"INSERT INTO customers (customer_id, customer_first_name, customer_second_name, customer_last_name, customer_birthdate, customer_country, customer_city, customer_phone, customer_email, customer_age, date_become_customer, customer_citizen_number, customer_username, customer_password) VALUES ({customerID}, '{customerStName}', '{customerNdName}', '{customerLastName}', '{customerBirthdate}', '{customerCountry}', '{customerCity}', '{customerPhone}', '{customerEmail}', '{customerAge}', '{dateBecomeCustomer}', '{customerCitizenNumber}', '{customerUsername}', '{customerPassword}')";
        try:
            cur.execute(query);
            connection.commit();

        except Exception as exc:
            print("ERROR trying to insert your data into the database! Consider contact us for possible solutions.");
            print(exc);

        finally:
            if connection:
                cur.close();
                connection.close();

    except Exception  as exc:
        print("Sorry, occurred some problem trying to insert your information into the database! Consider contact us for possible solutions.");
        print(exc);

def confirmNewUsername(un):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "password",
                                      host = "localhost",
                                      port = "5432",
                                      database = "databasename");
        cur = connection.cursor();
        query = f"SELECT customer_username FROM customers WHERE customer_username = '{un}'";
        cur.execute(query);
        count = cur.rowcount;
        if count == 0:
            return True;
        else:
            return False;
    except Exception as exc:
        print(exc);

def findCustomerUsernameFromDatabase(un):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "password",
                                      host = "localhost",
                                      port = "5432",
                                      database = "databasename");
        cur = connection.cursor();

        query = f"SELECT * FROM customers WHERE customer_username = '{un}'";
        count = 0;
        try:
            cur.execute(query);
            for row in cur:
                count += 1;

            if (count > 0):
                return True;
            else:
                return False;

        except Exception as exc:
            print(exc);

    except Exception as exc:
        print(exc);
    finally:
        if connection:
            connection.close();
            cur.close();

def findCustomerPasswordFromDatabase(un, pw):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "password",
                                      host = "localhost",
                                      port = "5432",
                                      database = "databasename");
        cur = connection.cursor();
        query = f"SELECT * FROM customers WHERE customer_username = '{un}' AND customer_password = '{pw}'";
        cur.execute(query);
        count = cur.rowcount
        if count > 0:
            return True;
        else:
            return False;

    except Exception as exc:
        print(exc);
    finally:
        if connection:
            connection.close();
            cur.close();

def findCustomerAccountFromCitizenNumber(citizenNumber, pw):
        try:
           connection = psycopg2.connect(user = "postgres",
                                      password = "password",
                                      host = "localhost",
                                      port = "5432",
                                      database = "databasename");
        cur = connection.cursor();
            try:            
                query = f"SELECT * FROM customers WHERE customer_citizen_number = '{citizenNumber}' AND customer_password = '{pw}'";
                cur.execute(query);
                count = cur.rowcount;
                if count == 1:
                    return True;
                else:
                    return False;
            except Exception as exc:
                print(exc);

        except Exception  as exc:
            print(exc);

def findAccountNumber(n):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "password",
                                      host = "localhost",
                                      port = "5432",
                                      database = "databasename");
        cur = connection.cursor();
        query = f"SELECT * FROM accounts WHERE account_number = {n}";
        cur.execute(query);
        count = 0;
        for rows in cur:
            count +=1;

        if count == 1:
            return True;
        else:
            return False;
    except Exception  as exc:
        print(exc);



class updateCustomer(databaseConnection):
    def __init__(self, connection, cur):
        self.connection = connection;
        self.cur = cur;

    def updateCustomerName(self, newFirstName, newSecondName, newLastName, username):
        try:
            query = f"UPDATE customers SET customer_first_name = '{newFirstName}', customer_second_name = '{newSecondName}', customer_last_name = '{newLastName}' WHERE customer_username = '{username}'";
            self.cur.execute(query);
            self.connection.commit();
            print("Name SUCCESSFULY updated!")
            sleep(0.5);
        except Exception as exc:
            print(exc);

    def updateCustomerBirthdateAndAge(self, newBirthdate, newAge, username):
        try:
            query = f"UPDATE customers SET customer_birthdate = '{newBirthdate}', customer_age = {newAge} WHERE customer_username = '{username}'";
            self.cur.execute(query);
            self.connection.commit();
            print("Birthdate SUCCESSFULY updated!");
            sleep(0.5);
        except Exception as exc:
            print(exc);

    def updateCustomerCountry(self, newCountry, username):
        try:
            query = f"UPDATE customers SET customer_country = '{newCountry}' WHERE customer_username = '{username}'";
            self.cur.execute(query)
            self.connection.commit();
            print("Country SUCCESSFULY updated!");
            sleep(0.5)
        except Exception as exc:
            print(exc);

    def updateCustomerCity(self, newCity, username):
        try:
            query = f"UPDATE customers SET customer_city = '{newCity}' WHERE customer_username = '{username}'";
            self.cur.execute(query)
            self.connection.commit();
            print("City SUCCESSFULY updated!");
            sleep(0.5);
        except Exception as exc:
            print(exc);

    def updateCustomerPhoneNumber(self, newPhoneNumber, username):
        try:
           query = f"UPDATE customers SET customer_phone = '{newPhoneNumber}' WHERE customer_username = '{username}'";
           self.cur.execute(query);
           self.connection.commit();
           print("Phone number SUCCESSFULY updated!");
           sleep(0.5);
        except Exception as exc:
            print(exc);

    def updateCustomerEmailAddress(self, newEmailAddress, username):
        try:
            query = f"UPDATE customers SET customer_email = '{newEmailAddress}' WHERE customer_username = '{username}'";
            self.cur.execute(query);
            self.connection.commit();
            print("Email address SUCCESSFULY updated!");
            sleep(0.5);
        except Exception as exc:
            print(exc);

    def updateCustomerUsername(self, newUsername, username):
        try:
            query = f"UPDATE customers SET customer_username = '{newUsername}' WHERE customer_username = '{username}'";
            self.cur.execute(query);
            self.connection.commit();
            print("Username SUCCESSFULY updated!");
            sleep(0.5);
        except Exception as exc:
            print(exc);

    def updateCustomerPassword(self, newPassword, username):
        try:
            query = f"UPDATE customers SET customer_password = '{newPassword}' WHERE customer_username = '{username}'";
            self.cur.execute(query);
            self.connection.commit();
            print("Password SUCCESSFULY updated!");
            sleep(0.5);
        except Exception as exc:
            print(exc);


class createBankAccount(databaseConnection):
    
    def __init__(self):
        super().__init__()

    def getNewAccountID(self):
        try:
            query = "SELECT account_id FROM accounts";
            self.cur.execute(query);
            count = self.cur.rowcount;
            return count;
        except Exception as exc:
            print(exc);
    
    # create a new bank account during the process of sign up;
    def createAccount(self, accountID, accountName, dateOpened, accountCode, initialDepositAmount, currentAmount, transactionLimit, currentNumberOfTransactions, customerID, accountState, accountGrade, accountNumber):
        try:
            query = f"INSERT INTO accounts (account_id, account_name, date_opened, account_code, initial_amount, current_amount, transactions_limit, current_number_transactions, customer_id, account_state, account_grade, account_number) VALUES ({accountID}, '{accountName}', '{dateOpened}', '{accountCode}', '{initialDepositAmount}', '{currentAmount}', '{transactionLimit}', '{currentNumberOfTransactions}', '{customerID}', '{accountState}', '{accountGrade}', {accountNumber})";
            self.cur.execute(query);
            self.connection.commit();
            print("Bank account SUCCESSFULY created");
            sleep(2);
        except Exception as exc:
            print(exc);

        finally:
            if self.connection:
                self.connection.close();
                self.cur.close();

    # create a new bank account after the process of sign up;
    
class removeAccount(databaseConnection):

    def __init__(self):
        super().__init__()

    def removeAccountFunction(self, un):
        try:
            query = f"DELETE FROM customers WHERE customer_username = '{un}'";
            self.cur.execute(query);
            self.connection.commit();
            return True
        except Exception as exc:
            print(exc);
            return False
        
        finally:
            if self.connection:
                self.connection.close();
                self.cur.close();

    # def removeBankAccountFunction(self, customerID):
    def removeBankAndAccountFunction(self, accountNumber, username):
        try:
            query = f"DELETE FROM accounts WHERE account_number = {accountNumber}";
            self.cur.execute(query);
            self.connection.commit();

            try:
                query = f"DELETE FROM customers WHERE customer_username = '{username}'";
                self.cur.execute(query);
                self.connection.commit();
                return True
            
            except Exception as exc:
                print(exc);
                return False

        except Exception as exc:
            print(exc);

        finally:
            if self.connection:
                self.connection.close();
                self.cur.close();

def checkAccountAmount(accountNumber):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "password",
                                      host = "localhost",
                                      port = "5432",
                                      database = "databasename");
        cur = connection.cursor();
        query = f"SELECT current_amount FROM accounts WHERE account_number = {accountNumber}";
        cur.execute(query);
    except Exception  as exc:
        print(exc);


class transactions(databaseConnection):

    def __init__(self):
        super().__init__()

    def createDeposit(self, accountNumber, depositAmount):
        try:
            query = f"SELECT current_amount FROM accounts WHERE account_number = {accountNumber}";
            self.cur.execute(query);
            rows = self.cur.fetchall();
            amount = rows[0]
            realAmount = amount[0]
            current_amount = realAmount + int(depositAmount)
            
            try:
                query = f"UPDATE accounts SET current_amount = {current_amount} WHERE account_number = {accountNumber}";
                self.cur.execute(query)
                self.connection.commit()
                print("Transaction SUCCESSFULY executed!");
            except Exception as exc:
                print("ERROR trying to execute the transaction! Contact us for possible solutions.")
                print(exc)
        
        except Exception as exc:
            print(exc);

        finally:
            if self.connection:
                self.connection.close()
                self.cur.close()

    def createWithdraw(self, accountNumber,  withdrawAmount):
        try:
            query = f"SELECT current_amount FROM accounts WHERE account_number = {accountNumber}";
            self.cur.execute(query);
            rows = self.cur.fetchall();
            amount = rows[0]
            realAmount = amount[0]
            while True:
                if realAmount >= int(withdrawAmount):
                    try:
                        currentAmount = realAmount - int(withdrawAmount)
                        query = f"UPDATE accounts SET current_amount = {currentAmount} WHERE account_number = {accountNumber}";
                        self.cur.execute(query);
                        self.connection.commit();
                        print("Transaction SUCCESSFULY executed!");
                    except Exception as exc:
                        print(exc)
                    break;
                else:
                    print("The value is higher than expected! Consider review the values and try again!")

        except Exception as exc:
            print(exc);
