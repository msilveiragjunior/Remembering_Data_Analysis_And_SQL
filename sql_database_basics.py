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
