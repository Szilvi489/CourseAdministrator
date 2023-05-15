import json
import random
from datetime import datetime

from db import load_data


class UserAuth:
    def __init__(self, db_file):
        self.db_file = db_file
        self.data = load_data()

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for user in self.data['accounts']:
            if user['username'] == username and user['password'] == password:
                print(f"Welcome, {user['first_name']} {user['last_name']}!")
                return True
        print("Invalid username or password.")
        return True

#Creating helpful little methods for the register method:

    #we create an email to the user out of their first name, last name and some sting we want to add
    def create_mail(self, first_name, last_name):
        email = first_name.lower + "_" + last_name.lower() + "@" + "fh-campus.com"
        return email
    #create a registration date to the user, they dont have to type it in manually, we will save it automatically
    def registration_date(self):
        registration_date = datetime.now().strftime("%d-%m-%Y")
        return registration_date

    #create a username to the user, so they dont have to create their own, we will try to create a unique username
    #later we can implement, that this method should check the database if the username exists, if so
    #try to create it again, or give the option, to type something manually...
    def create_username(self, first_name, last_name):
        registration_date = self.registration_date().replace('-', '')
        year = registration_date[-2:]
        username = first_name.lower() + "_" + last_name.lower() +"_"+ registration_date[:-4] + year
        return username

    #create a password to our user out of the first name, last name and some random number
    def create_password(self, first_name, last_name):
        #first_name=John, last_name=Doe
        #pwJohnD445
        randomNumber = random.randint(100, 999)
        password = "pw" + first_name + last_name[0] + str(randomNumber)
        return password


    def register(self):

        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        account_type = input("Enter your account type (user or admin): ")
        #classes = input("Enter your classes (comma-separated list): ").split(",")
        type_specific_data = {}
        if account_type == "user":
            address = input("Enter your address: ")
            phone = input("Enter your phone number: ")
            type_specific_data = {
                'type': 'student',
                'address': address,
                'phone': phone
            }
        elif account_type == "admin":
            acc_level = input("Enter your access level: ")
            type_specific_data = {
                'type': 'admin',
                'level': acc_level
            }

        email = self.create_mail(first_name, last_name)
        username = self.create_username(first_name,last_name)
        password = self.create_password(first_name,last_name)

        new_account = {
            'id': len(self.data['accounts']) + 1,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'username': username,
            'password': password,
            'type': account_type,
            #'classes': [int(c) for c in classes],
            'type_specific_data': type_specific_data
        }
        self.data['accounts'].append(new_account)
        self.save_data()
        print("Account created successfully!")

    def save_data(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.data, f)

