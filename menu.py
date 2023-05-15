from authentication import UserAuth

auth = UserAuth('data/data.json')

def mainMenu():
    print("Hello!")
    print("Do you have an account? \n If you would like to log in, type: \" l \" \n If you would like to register, type: \" r \"")
    userInput = input()
    userInput = userInput.lower()
    if isinstance(userInput,str):
        if userInput == "l":
            print("*****LOG IN***** ")
            auth.login()
        if userInput == "r":
            print("*****REGISTER*****")
            auth.register()






