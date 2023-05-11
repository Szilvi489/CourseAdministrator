import data

def testDatabase():
        # Connect to the database
    cnx = data.connect()
    if cnx is None:
        return

    # Create a cursor object
    cursor = cnx.cursor()

    # Test CRUD operations
    #data.create_account(cursor, 13, "Szilvia Varga", "123 Stuwer Strasse", "676-1234")
    #data.update_account(cursor, 1, "456 Oak Ave")
    #data.delete_account(cursor, 11)
    #data.read_accounts(cursor)
    #data.read_accountsFormatted(cursor)
    #data.read_users(cursor)
    #data.account_exists(cursor, "Emma Jones")

     # Commit changes and close the cursor and connection
    cnx.commit()
    cursor.close()
    cnx.close()

testDatabase()
