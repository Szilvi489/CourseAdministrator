import json

import data
from authentication import UserAuth

#OUTDATED!!!
def testDatabase():#testing the old database
        # Connect to the database
    cnx = data.connect()
    if cnx is None:
        return

    # Create a cursor object
    cursor = cnx.cursor()

    # Test CRUD operations
    #data.create_account(cursor, 13, "Szilvia Varga", "123 Stuwer Strasse", "676-1234")
    data.update_account(cursor, 3, "456 Oak Ave")
    #data.delete_account(cursor, 11)
    #data.read_accounts(cursor)
    #data.read_accountsFormatted(cursor)
    #data.read_users(cursor)
    #data.account_exists(cursor, "Emma Jones")

     # Commit changes and close the cursor and connection
    cnx.commit()
    cursor.close()
    cnx.close()

#testDatabase()

def load_data():
    with open('data/data.json', 'r') as f:
        data = json.load(f)
    return data

def testDatabase():
#CRUD METHODS:

#CREATE
 # Create a new account
    def create_account():
     data=load_data()
    # Get the accounts data
     accounts = data['accounts']

     new_account = {
            'id': len(accounts) + 1, # auto increment --> this will simply set the id to the next number (assuming no changes happened in the db...)
            'first_name': 'Kelly',
            'last_name': 'Mann',
            'email': 'kelly_mann@example.com',
            'username': 'kellymann',
            'password': 'pwKelly663',
            'type': 'user',
            'classes': [1],
            'type_specific_data': {
                'type': 'student',
                'address': '123 Main St',
                'phone': '555-1234'
            }
        }

     accounts.append(new_account)

     # Write the updated data back to the file
     with open('data/data.json', 'w') as f:
        json.dump(data, f)

    create_account()

#READ :
    #print all the data we have nicely formatted
    def print_data_formatted():
     data=load_data()
     print(json.dumps(data, indent=4))

    #print_data_formatted()

    #print all the Accounts
    def print_accounts():
     data=load_data()
     accounts=data['accounts']
     for account in accounts:
       print(account)

    print_accounts()

    #print only the firstname of the first account
    def print_account():
     data=load_data()
     accounts = data['accounts']
     # Print the first account's first name
     print(accounts[1]['first_name'])

    #print_account()

testDatabase()
def testAuthenticationClass():
    user_auth = UserAuth('db.json')
    def testRegistrationDate():

     registration_date = user_auth.registration_date()
     print("Type: " + str(type(registration_date)) +" Date: "+ str(registration_date))

    #testRegistrationDate()

    def testCreateUsername():
        firstN= "Luluu"
        lastN= "Lallaaa"
        username = user_auth.create_username(firstN,lastN)
        print(username)
    #testCreateUsername()

    def testCreatePassword():
        firstN= "John"
        lastN= "Doe"
        pasword = user_auth.create_password(firstN,lastN)
        print(pasword)
    #testCreatePassword()


#testAuthenticationClass()
