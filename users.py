import table_01_sql
import sqlite3


# --- Beginning SQL with Python --- #

# --- Here we'll insert each user to it's table --- #
# Let's create a new table. The module sqllite3 can create
# a new file with the method connect, that establishes a connection
# to the db. If the file does not exist, it creates a new one.
# Or you can use the DB Browser to create it, if you don't want to
# create the database here.
# We'll only use this db with the first 3 examples
# connection = sqlite3.connect('users.db')
connection = sqlite3.connect('hubway.db')
# We have to create an object called cursor that will allow us
# to execute SQL commands.
cursor = connection.cursor()

# Here we'll loop through a the main program, adding the keys
# and values
numbers_of_keys = input("Please, specify the number of keys inside each "
                        "user: \n")
table_01 = {
    }


# Here we call the create table function
def create_table_function():
    for i in range(0, int(numbers_of_keys)):
        key = input("Insert the name of the key \n")
        table_01[key] = input("Insert a value for the key \n")
    # Here we add the values to their keys
    keys_dict = list(table_01.keys())
    create_table = table_01_sql.create_table(keys_dict[0], keys_dict[1],
                                             keys_dict[2], keys_dict[3])
    print(create_table)
    cursor.execute(create_table)


# Here we call the insert function.
def insert_user_function():
    for i in range(0, int(numbers_of_keys)):
        key = input("Insert the name of the key \n")
        table_01[key] = input("Insert a value for the key \n")
    # Here we add the values to their keys
    keys_dict = list(table_01.keys())
    # number_of_users = input("Insert the number of users: \n")

    insert_user = table_01_sql.insert_user(keys_dict[0], keys_dict[2],
                                           keys_dict[3],
                                           table_01[keys_dict[2]],
                                           table_01[keys_dict[3]])
    # Here we are executing the command insert inside the variable insert_user
    cursor.execute(insert_user)


# Here we we'll call the function for the SELECT method.
# We'll select the column usernames, select them and, then,
# print every single one of them. The return of this execute()
# method will be a tuple of all information available.
def select_user_function():
    key = input("Enter the name of the table from which you want the"
                " information: \n")
    column_01 = input("Enter the column name:\n")
    # Now we can send the information to create the statement
    # necessary with a function, inside the file table_01_sql
    select_user = table_01_sql.select_username(column_01, key)
    cursor.execute(select_user)
    # With the fetchall() method we can retrieve all the information
    # within the database.
    rows = cursor.fetchall()
    # With this for loop we can print each information from
    # the tuple retrieved.
    for i in rows:
        print(i)


# Here we'll test the SELECT DISTINCT statement
def select_distinct_function():
    key = input("Enter the name of the table from which you want the"
                " information: \n")
    column_01 = input("Enter the column name:\n")
    distinct_municipality = table_01_sql.select_distinct_function(key,
                                                                  column_01)
    cursor.execute(distinct_municipality)
    rows = cursor.fetchall()
    for i in rows:
        print(str(*i) + "\n")

    # Here we show the count for SELECT DISTINCT municipalities
    distinct_municipality = table_01_sql.select_distinct_function(key,
                                                                  column_01,
                                                                  False)
    cursor.execute(distinct_municipality)
    rows = cursor.fetchall()
    for i in rows:
        print(str(*i) + "\n")


# Here we'll test the WHERE clause with SELECT with some examples
def select_with_where():
    key = input("Enter the name of the table from which you want the"
                " information: \n")
    column_01 = input("Enter the column name: \n")
    condition = input("Enter the operator symbol with the condition: \n")
    where_municipality = table_01_sql.select_where_function(key, column_01,
                                                            condition)
    print(where_municipality)
    cursor.execute(where_municipality)
    rows = cursor.fetchall()
    for i in rows:
        print(*i)


select_with_where()
# select_distinct_function()
# select_user_function()
# The commit method is used to end the transaction making changes in the
# database permanent
connection.commit()
# Here we use the close(), and the connection method from the class cursor to
# close any connection available to the database.
cursor.close()
connection.close()
