import sqlite3 # Importing the sqlite3 module

#connection = sqlite3.connect(":memory:") # Creates a database in memory

connection = sqlite3.connect("customer.db") # Creates a database file

c = connection.cursor() # Create a cursor

# Create a table using docstrings
c.execute("""CREATE_TABLE customers (
            first_name DATATYPE,
            last_name DATATYPE,
            email DATATYPE
    )""")


