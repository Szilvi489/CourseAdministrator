from user import User


class Teacher(User):
    def __init__(self,first_name, last_name,email, username, password,classes, type_specific_data):
        super.__init__(first_name, last_name,email, username, password,classes,type_specific_data="Student")
