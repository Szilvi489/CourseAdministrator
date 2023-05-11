import data

def sayHello():
    print("Hello!")
    print("Do you have an account? \n If you would like to log in, type: \" l \" \n If you would like to register, type: \" r \"")
    userInput = input()
    userInput = userInput.lower()
    if isinstance(userInput,str):
        if userInput == "l":
            print("*****LOG IN***** ")
            login()
        if userInput == "r":
            print("*****REGISTER*****")
            register()

#todo
def register():
     print("Please enter your Username:")
     username = input()
     if isinstance(username,str):
        print("Hello " + username + "!")




def login():
    cursor = data.connection()
    print("Please enter your Username: \n")
    username = input()
    print("Please enter your Password: \n")
    password = input()

    if isinstance(username, str):
        if data.account_exists(username,password)==True:
            print(type(username))
            takeFirstName = username.split("_")[0].capitalize()
            print("Hello " + takeFirstName + "!")

        if data.account_exists(username)== False:
            print("I cannot find your username " + username + "!")



