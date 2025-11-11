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
    insert_user_table = "SELECT {} from {};".format(column, table)
    return insert_user_table
