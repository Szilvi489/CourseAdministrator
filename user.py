from account import Account
from db import Database


class User(Account):
    def __init__(self, first_name="", last_name="", email="", username="", password="", type="", classes="", type_specific_data="", db_file=""):
         super().__init__(classes, type_specific_data, type="User")
         self.classes = classes
         self.data = self.db.load_data()


#all users are able to do certain things...
#for example search other users
    def search_users(self, **kwargs):
        users = self.data['accounts']
        for key, value in kwargs.items():
            users = [user for user in users if user.get(key) == value]
        print("YES")
        return users

