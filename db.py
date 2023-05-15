import json
class Database:
    def __init__(self,filename):
        self.filename = filename

# Load the JSON data from a file in the 'data' directory
    def load_data(self):
        with open('data/data.json', 'r') as f:
            data = json.load(f)
        return data



def print_admins():
 data=load_data()
 accounts = data['accounts']

 # Filter the accounts to only include administrators
 administrators = [account for account in accounts if account['type'] == 'admin']

# Print all the administrators
 for administrator in administrators:
    print(administrator)

def find_by_mail():
 data=load_data()
 accounts = data['accounts']
# Read an account by email address
 email = "jared_leto@fh-campus.com"
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
 data=load_data()
 courses = data['courses']
 # Print the name of the first course
 print(courses[0]['name'])


def print_classes():
 data=load_data()
 classes = data['classes']
 # Print the name of the first class
 print(classes[0]['name'])


#UPDATE
# Update name in an account by email address
def update_by_mail():
    data=load_data()
    # Get the accounts
    accounts = data['accounts']

    # Update an account by email address
    email = "emma_wattson@fh-campus.com"
    for acc in accounts:
        if acc['email'] == email:
            acc['first_name'] = 'Emmmammimalie'
            acc['last_name'] = 'Wattsonnelsonna'
            break

    # Write the updated data back to the file
    with open('data/data.json', 'w') as f:
        json.dump(data, f)

#Delete
def delete_by_email():
    data=load_data()
    accounts = data['accounts']
    # Delete an account by email address
    email = "jared_leto@fh-campus.com"
    for acc in accounts:
        if acc['email'] == email:
            accounts.remove(acc)
            break

    with open('data/data.json', 'w') as f:
       json.dump(data, f)


#print_data_formatted()
#print_accounts()
#print_admins()
#create_account()
#find_by_mail()
#delete_by_email()
#update_by_mail()


