import json

# Load the JSON data from a file in the 'data' directory
with open('data/data.json', 'r') as f:
    data = json.load(f)

#CRUD:

#CREATE

 # Create a new account
def create_account():
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

#READ :
def print_data_formatted():
 print(json.dumps(data, indent=4))

def print_accounts():
    accounts=data['accounts']
    for account in accounts:
        print(account)

def print_account():
 accounts = data['accounts']
 # Print the first account's first name
 print(accounts[0]['first_name'])

def print_admins():
 accounts = data['accounts']

 # Filter the accounts to only include administrators
 administrators = [account for account in accounts if account['type'] == 'admin']

# Print all the administrators
 for administrator in administrators:
    print(administrator)

def find_by_mail():
 accounts = data['accounts']
# Read an account by email address
 email = 'emma_wattson@fh-campus.com'
 account = None
 for acc in accounts:
    if acc['email'] == email:
        print("we have it")
        account = acc
        break

 if account is None:
    print('Account not found')
 else:
    print(account)
def print_course():
 courses = data['courses']
 # Print the name of the first course
 print(courses[0]['name'])


def print_classes():
 classes = data['classes']
 # Print the name of the first class
 print(classes[0]['name'])


#UPDATE
# Update an account by email address
def update_by_mail():
 accounts = data['accounts']
 email = 'john_doe@example.com'
 for acc in accounts:
    if acc['email'] == email:
        acc['first_name'] = 'Jane'
        acc['last_name'] = 'Doe'
        break


#print_data_formatted()
#print_accounts()
#print_admins()
#create_account()
find_by_mail()


