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
    cursor.execute(where_municipality)
    rows = cursor.fetchall()
    for i in rows:
        print(*i)


# Here we'll test the SELECT FROM ORDER BY keyword statement
def select_orderby_function():
    key = input("Enter the name of the table from which you want the"
                " information: \n")
    column_01 = input("Enter the column name:\n")
    # Let's place a flag to order by asc or desc
    condition = input("Enter 'asc' for ascending order or"
                      " 'desc' for descending order: \n")
    flag = False
    flag_is = input("Do you want to insert the condition? \n"
                    "Type no for False and yes for True: \n")
    if flag_is.lower() == 'yes':
        flag = True
    else:
        flag = False
    distinct_municipality = table_01_sql.select_orderby_function(key,
                                                                 column_01,
                                                                 condition,
                                                                 flag)
    cursor.execute(distinct_municipality)
    rows = cursor.fetchall()
    for i in rows:
        print(*i)


# With this function we'll test if a query returns empty or not,
# and we'll see how many fields are empty
def check_null_or_not_null():
    key = input("Enter the name of the table from which you want the"
                " information: \n")
    column_01 = input("Enter the column name: \n")
    condition = input("Enter IS NULL or IS NOT NULL: \n")
    null_not_null = table_01_sql.check_null_or_not_null(key, column_01,
                                                        condition.upper())
    print(null_not_null)
    cursor.execute(null_not_null)
    rows = cursor.fetchall()
    if condition == 'IS NOT NULL':
        print("These are the returns for {} IS NOT NULL\n".format(column_01))
        for row in rows:
            print(*row)
    elif condition == 'IS NULL':
        print("These are the returns for {} IS NULL\n".format(column_01))
        for row in rows:
            print(*row)


# Now we'll use the function to show how the LIKE operator works:
def like_operator():
    key = input("Enter the name of the table from which you want the"
                " information: \n")
    column_01 = input("Enter the column name: \n")
    condition = input("Enter the condition in between apostrophes (''): \n")
    like_op = table_01_sql.like_operator(key, column_01, condition)
    cursor.execute(like_op)
    rows = cursor.fetchall()
    for i in rows:
        print(*i, "\n")


# Here we'll define the function that will carry the code for the IN
# Operator:
def in_operator():
    values = []
    key = input("Enter the name of the table from which you want the"
                " information: \n")
    column_01 = input("Enter the column name: \n")
    num_of_values = input("Enter the number of values: \n")
    for i in range(0, int(num_of_values)):
        values.append(input("Enter the name of the value: \n"))
    in_op = table_01_sql.in_operator(key, column_01, values)
    print(in_op)
    cursor.execute(in_op)
    rows = cursor.fetchall()
    for i in rows:
        print(*i, "\n")


# Here we're defining the function that will codify our SELECT INTO
# statement. It will join the the above example of the IN operator.
# def into_clause():
#    name_of_database = input("Enter the name of the db where you want"
#                             " to enter the new table: \n")
#    key = input("Enter the name of the table from which you want the"
#                " information: \n")
#    print("The default SELECT is * (all).")
#    condition = input("Enter the condition in between apostrophes (''): \n")
#    select_into = table_01_sql.into_clause(name_of_database, key, condition)
#    print(select_into)
#    rows = cursor.fetchall()
#    for i in rows:
#        print(*i, "\n")
# Well, just remembered this does not work with sqlite. haha

# Here we're altering the table to our needs. In this case, we're renaming
# the table and checking, with PRAGMA - SQLite specific command - to
# see if the new table exists. If exists, we'll fetch its rows.
# If rows are returned, we print that the table exists with the new name.
# Otherwise, we print that the table does not exist.
def alter_table():
    key = input("Enter the name of the table from which you want the"
                " information: \n")
    key_name = input("Enter the new name for the table: \n")
    alter_name = f'ALTER TABLE "{key}" RENAME TO "{key_name}"'
    print(alter_name)
    try:
        cursor.execute(alter_name)
        print(f'Table "{key}" has been renamed to "{key_name}"')
    except sqlite3.Error as e:
        print("This error occurred: ", e)
    cursor.execute(f'PRAGMA table_info ("{key_name}");')
    rows = cursor.fetchall()
    if rows:
        print("Table exists now with the new name.\n")
    else:
        print("The table does not exist.\n")


# Here we're getting the information necessary to create our view.
# But also let's create a SELECT * to view the rows inside our view.
def create_view():
    key = input("Enter the name of the table from which you want the"
                " information: \n")
    key_name = input("Enter the name for the view: \n")
    column_01 = input("Enter the column name: \n")
    condition = input("Enter the condition: \n")
    # We could parameterize the string with this representation:
    # view = f'CREATE VIEW "{key_name}" AS \
    #         SELECT "{column_01}"\
    #         FROM "{key}"\
    #         WHERE {condition}'
    # print(view)
    # This would mitigate SQL Injection attempts
    # But for the sake of clarity, we'll send it to another function to
    # the job of creating the concatenating the statement
    view = table_01_sql.create_view(key, key_name, column_01, condition)
    print(view + "\n")
    cursor.execute(view)

    # Here we'll create the SELECT statement with a parameterized version
    # of the string
    query = f'SELECT * FROM "{key_name}";'
    cursor.execute(query)
    rows = cursor.fetchall()
    for i in rows:
        print(*i, "\n")


create_view()
# alter_table()
# into_clause()
# in_operator()
# like_operator()
# check_null_or_not_null()
# select_orderby_function()
# select_with_where()
# select_distinct_function()
# select_user_function()
# The commit method is used to end the transaction making changes in the
# database permanent
connection.commit()
# Here we use the close(), and the connection method from the class cursor to
# close any connection available to the database.
cursor.close()
connection.close()
