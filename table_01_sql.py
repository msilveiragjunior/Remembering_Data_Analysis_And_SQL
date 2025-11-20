# This is the file for the sql functions.

def create_table(table_name, index, username, email):
    create_user_table = 'CREATE TABLE {} (' \
                         '{} INTEGER PRIMARY KEY AUTOINCREMENT,' \
                         '{} TEXT,' \
                         '{} TEXT,' \
                        ')'.format(table_name, index, username, email)
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
def select_orderby_function(table, column, condition, flag):
    # Here we'll define the command using the syntax given
    # on the sql_explaining file.
    if flag:
        select_order_by = "SELECT {} " \
                        "FROM {} " \
                        "ORDER BY {} {}".format(column, table, column,
                                                condition)
        return select_order_by
    else:
        select_order_by = "SELECT {} " \
                        "FROM {} " \
                        "ORDER BY {}".format(column, table, column)
        return select_order_by


# Here we'll define the function to check if NULL or NOT NULL:
def check_null_or_not_null(table, column, condition):
    check_null = "SELECT * " \
                 "FROM {} " \
                 "WHERE {} {};".format(table, column, condition)
    return check_null


# Here we'll structure the function to use the LIKE operator:
def like_operator(table, column, condition):
    like_op = "SELECT * " \
              "FROM {} " \
              "WHERE {} LIKE {};".format(table, column, condition)
    return like_op


# Now we'll structure the function for the IN operator:
# Remember, it's not parameterized, so it's flawed with the
# possibility of SQL injection. So parameterize your queries
# when doing it
def in_operator(table, column, value):
    string = ", ".join(f"'{val}'" for val in value)
    in_op = "SELECT * " \
            "FROM {} " \
            "WHERE {} IN ({});".format(table, column, string)
    return in_op


# We've done the in_operator before. Now we'll mix it with
# the INTO clause, to copy everything into a new table, inside
# another database.
# def into_clause(name_of_database, table, condition):
#    into_clause = "SELECT * " \
#                  "INTO new_table [IN {}]" \
#                  "FROM stations " \
#                  "WHERE {} IN ({});".format(name_of_database, table,
#                                             condition)
#    return into_clause
# Just remembered the IN database does not work with python. We
# need so send a new cursor, by establishing a new connection
# with the database and, then, sending the cursor as an object to the function.
# By doing this, we are able to deal with this unfortunate problem.


# We've done almost the same operation when we created a table.
# However, this time, we are creating a view, by selecting columns
# from the table that we've created. We could create a *column argument,
# to receive a tuple of columns, but one column, for this example,
# is enough.
def create_view(table, view_name, column, condition):
    view = "CREATE VIEW {} AS " \
           "SELECT {} " \
           "FROM {} " \
           "WHERE {};".format(view_name, column, table, condition)
    return view
