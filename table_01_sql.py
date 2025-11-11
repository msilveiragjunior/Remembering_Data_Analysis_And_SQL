# This is the file for the sql functions.

def create_table(table_name, index, username, email):
    create_user_table = 'CREATE TABLE {} (' \
                         '{} INTEGER PRIMARY KEY,' \
                         '{} TEXT,' \
                         '{} TEXT,' \
                         'PRIMARY KEY ({} AUTOINCREMENT)' \
                        ')'.format(table_name, index, username, email, index)
    return create_user_table
# Here we'll insert users into the table. We can consult the results
# With DB Browser to see the users inserted


# The INSERT INTO command tells the database to insert into a table,
# then we tell the name of the columns, in between parenthesis, and
# the VALUES, also in between parenthesis and with a comma, separating
# all values, that will be inserted in those columns.
# As our table auto-increments its PRIMARY KEY, we don't need to
# create an increment to the id, that act as an integer and index.
# As it auto-increments itself, the SQL database will send an statement
# to increment a value before the insertion of the new row.
def insert_user(table_name, username, email, value_username, value_email):
    insert_user_table = "INSERT INTO {} (" \
                        "{}, " \
                        "{}) " \
                        "VALUES ('{}','{}'" \
                        ");".format(table_name, username, email,
                                    value_username,
                                    value_email)
    return insert_user_table


# Here we'll select the column from the table and return the string
# formatted.
def select_username(column, table):
    select_username_table = "SELECT {} FROM {};".format(column, table)
    return select_username_table


# Here we'll define the select distinct function
def select_distinct_function(table, column):
    select_distinct = "SELECT DISTINCT {} FROM {};".format(column, table)
    return select_distinct
