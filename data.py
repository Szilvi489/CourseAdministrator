import mysql.connector

# Establish database connection
def connect():
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            port=55013,
            password="bp92",
            database="CourseAdministrator.db"
        )
        #print("Connected to the database")
        return cnx
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None

# Create a new record in the Account table
def create_account(cursor, account_id, name, address, telephone,email,password,username):
    query = "INSERT INTO Account (account_id, name, address, telephone,email,password,username) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (account_id, name, address, telephone, email, password, username)
    cursor.execute(query, values)
    print("Account created successfully")


# Read all records from the Account table
def read_accounts(cursor):
    query = "SELECT * FROM Account"
    cursor.execute(query)
    accounts = cursor.fetchall()
    for account in accounts:
        print(account)

# Read all records from the Account table
def read_accountsFormatted(cursor):
    query = "SELECT * FROM Account"
    cursor.execute(query)
    accounts = cursor.fetchall()
    for account in accounts:
        print("Account ID:", account[0])
        print("Name:", account[1])
        print("Address:", account[2])
        print("Telephone:", account[3])
        print("Email:", account[4])
        print("Password", account[5])
        print("Username", account[6])
        print()  # Print an empty line between records

def read_users(cursor):
    query = "SELECT *FROM Account JOIN User ON User.account_id = Account.account_id"
    cursor.execute(query)
    users = cursor.fetchall()
    for user in users:
        #print(user)
        print("Name:", user[1])
        print("Address:", user[2])
        print("Telephone:", user[3])
        print()  # Print an empty line between records

def account_exists(username, password):
    cnx = connect()
    if cnx is None:
        return False

    try:
        cursor = cnx.cursor()
        query = "SELECT * FROM Account WHERE username = %s"
        values = (username,)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            stored_password = result[4]  # Assuming password is stored in the 5th column
            if password == stored_password:
                print("Username and password match!")
                return True
            else:
                print("Password is incorrect.")
                return False
        else:
            print("Username does not exist.")
            return False

    finally:
        cursor.close()
        cnx.close()



# Update an existing record in the Account table
def update_account(cursor, account_id, new_address):
    query = "UPDATE Account SET address = %s WHERE account_id = %s"
    values = (new_address, account_id)
    cursor.execute(query, values)
    print("Account updated successfully")

# Delete a record from the Account table
def delete_account(cursor, account_id):
    # Delete the admin record(s) referencing the account
    delete_admin_query = "DELETE FROM Admin WHERE account_id = %s"
    delete_admin_values = (account_id,)
    cursor.execute(delete_admin_query, delete_admin_values)

    # Delete the account
    delete_account_query = "DELETE FROM Account WHERE account_id = %s"
    delete_account_values = (account_id,)
    cursor.execute(delete_account_query, delete_account_values)

    print("Account deleted successfully")


# Main function to test the database connection and CRUD operations
def connection():
    # Connect to the database
    cnx = connect()
    if cnx is None:
        return None

    # Commit changes and close the connection
    cnx.commit()
    cnx.close()

    return cnx
