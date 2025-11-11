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
def select_distinct_function(table, column, flag=True):
    if flag:
        select_distinct = "SELECT DISTINCT {} FROM {};".format(column, table)
        return select_distinct
    else:
        select_distinct = "SELECT COUNT(DISTINCT {}) FROM {};".format(column,
                                                                      table)
        return select_distinct


# Here we'll define the select with where clause function
def select_where_function(table, column, condition):
    # Here we define the command SELECT with the wildcard symbol *
    # to select all queries from a table
    select_distinct = "SELECT * " \
                      "FROM {} " \
                      "WHERE {}{};".format(table, column, condition)
    return select_distinct


# Here we'll use the keyword ORDER BY to define our function:
def select_orderby_function(table, column, condition):
    # Here we'll define the command using the syntax given
    # on the sql_explaining file.
    select_order_by = "SELECT {}" \
                      "FROM {} " \
                      "ORDER BY {} {}".format(column, table, column, condition)
    return select_order_by
