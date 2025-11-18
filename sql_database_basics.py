# --- SQL Databases - A synthesis of the basics --- #
"""
When we began this repo, we tried to cover the basics of the structure of SQL:
the inner workings, its definitions, statements, clauses, keywords, operators
and so on. We've got to know how to manipulate the data inside the database,
but not how to manipulate the database - other than creating it, creating a
table and other minor examples. However, it was necessary for our understanding
that we create it, so we could go on with our little adventure. So now we need
to construct a solid framework on how to create, alter and maintain a database.
So let's begin.
"""
# --- CREATE DATABASE --- #
"""
When we need to create a database, we need it to store our tables,
views, and functions. Everything will go inside it.
This section is simple. We just need to show the syntax to create a database:
CREATE DATABASE database;
We've created a function inside table_01_sql.py to show how to create a
table, but not a database.
Applying it to a real case - this would apply to PostgreSQL:
CREATE DATABASE stations;
This would create a database called stations.
We can't use the same statement with SQLite. With SQLite, we
use the method connect() from sqlite3, for example:
connection = sqlite3.connect('database.db')
This would create a connection to a given database, and would
create the file if it didn't exist before.
To summarize: CREATE DATABASE creates a new SQL database.
PS: To check if the database was created, we need to use the statement
SHOW DATABASES - this will work with MySQL.
It will return the name of the databases in our server.
PostgreSQL uses \\l inside psql, and SQLite shows databases inside our
directory.
"""
# --- DROP DATABASE --- #
"""
The DROP DATABASE statement in SQL is used to delete a database permanently:
all its data and information stored, along with the database itself.
The syntax is as follows:
DROP DATABASE database;
PS:
Without a backup, all data will be lost.
So it's a permanent action executed by our database management system
(DBMS).
"""
# --- BACKUP DATABASE --- #
"""
We can use the BACKUP DATABASE statement in SQL Server to create
a complete backup of a given database.
The syntax is as follows:
BACKUP DATABASE database
TO DISK = 'name_of_the_path';
We can also update the contents of the database with the
DIFFERENTIAL clause.
The syntax would look like this:
BACKUP DATABASE database
TO DISK = 'name_of_the_path'
WITH DIFFERENTIAL;
A real case example would look like this:
BACKUP DATABASE stations
TO DISK = 'E:\\Databases\\stations.bak';
Then, to save only the changes made since that backup, we would do this:
BACKUP DATABASE stations
TO DISK = 'E:\\Databases\\stations.bak'
WITH DIFFERENTIAL;
PS:
PostgreSQL uses its own backup tools (such as `pg_dump`),
so it does not support the BACKUP DATABASE statement.
SQLite databases can be backed up using its CLI or by copying
the database file directly (e.g., with Python:
with open('database.db', 'rb') as src, open('backup.db', 'wb') as dst:
    dst.write(src.read()));
With the SQLite CLI installed, we can also use:
sqlite3 database.db ".backup database_backup.db".
"""
# --- CREATE TABLE --- #
"""
Now we enter a realm where we can use Python to manipulate the database:
one where we can send strings with statements to create a table.
The CREATE TABLE statement is fully functional within the SQLite framework.
The syntax is as follows:
CREATE TABLE table (
    column datatype,
    column_02 datatype,
    column_03 datatype);
We've covered the creation of a table using Python inside the file
table_01_sql.py:
def create_table(table_name, index, username, email):
    create_user_table = 'CREATE TABLE {} (' \
                         '{} INTEGER PRIMARY KEY AUTOINCREMENT,' \
                         '{} TEXT,' \
                         '{} TEXT' \
                        ')'.format(table_name, index, username, email)
    return create_user_table;
We can also create a table using another table, and I'm pretty sure
we've covered it in the sql_basics.py file.
But, for the sake of consistency, let's show the syntax:
CREATE TABLE new_table AS
    SELECT *
    FROM table;
PS:
Remember, this is not a parameterized string, so it's possible
to use SQL Injection to manipulate its data. We are using
the code above just to clarify each aspect of the
CREATE TABLE statement.
"""
# --- DROP TABLE --- #
"""The DROP TABLE statement in SQL is used to delete a table permanently:
all its data and information stored, along with the table itself.
The syntax is as follows:
DROP TABLE table;
We can also remove only the data inside a table with the
TRUNCATE TABLE statement.
This statement deletes the data inside the table, but not the table.
PS:
Without a backup, all data will be lost.
So it's a permanent action executed by our database management system
(DBMS).
"""
