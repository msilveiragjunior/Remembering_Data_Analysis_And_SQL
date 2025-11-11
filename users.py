import table_01_sql
import sqlite3


# --- Beginning SQL with Python --- #

# --- Here we'll insert each user to it's table --- #
# Let's create a new table. The module sqllite3 can create
# a new file with the method connect, that establishes a connection
# to the db. If the file does not exist, it creates a new one.
# Or you can use the DB Browser to create it, if you don't want to
# create the database here.
connection = sqlite3.connect('users.db')

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
        key = input("Insira o nome da chave: \n")
        table_01[key] = input("Insira um valor para a chave: \n")
    # Here we add the values to their keys
    keys_dict = list(table_01.keys())
    create_table = table_01_sql.create_table(keys_dict[0], keys_dict[1],
                                             keys_dict[2], keys_dict[3])
    print(create_table)
    cursor.execute(create_table)


# Here we call the insert function.
def insert_user_function():
    for i in range(0, int(numbers_of_keys)):
        key = input("Insira o nome da chave: \n")
        table_01[key] = input("Insira um valor para a chave: \n")
    # Here we add the values to their keys
    keys_dict = list(table_01.keys())
    # number_of_users = input("Insert the number of users: \n")

    insert_user = table_01_sql.insert_user(keys_dict[0], keys_dict[2],
                                           keys_dict[3],
                                           table_01[keys_dict[2]],
                                           table_01[keys_dict[3]])
    # Here we are executing the command insert inside the variable insert_user
    cursor.execute(insert_user)


# The commit method is used to end the transaction making changes in the
# database permanent
connection.commit()
# Here we use the close() method from the class cursor to close any connection
# available to the database
cursor.close()
