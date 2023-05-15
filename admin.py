from account import Account


class Admin(Account):

    def __init__(self,first_name, last_name,email, username, password, type, level):
        super.__init__(level,type="Admin")
        self.level = level



