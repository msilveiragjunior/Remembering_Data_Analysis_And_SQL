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
To maintain consistency, the syntax is as follows:
TRUNCATE TABLE table;
This statement deletes the data inside the table, but not the table.
PS:
Without a backup, all data will be lost.
So it's a permanent action executed by our database management system
(DBMS).
"""
# --- ALTER TABLE --- #
"""
The ALTER TABLE statement is used to add, drop constraints from a table but,
also, is used to add, delete, or modify columns in a table.
While using SQLite, ALTER TABLE statement is difficult to use, all because
the way SQLite implements a schema.
With SQL Server, we can ADD and DROP a column; also ALTER a datatype
and RENAME a table.
The syntaxes are as follows:
ALTER TABLE table
ADD column datatype; <---- This will work with SQLite
This will add a new column with a specific datatype.
ALTER TABLE table
DROP COLUMN column; <---- This will work with SQLite
This will delete a column in a table.
ALTER TABLE table
RENAME COLUMN old_name to new_name; <---- This will work with SQLite
This will rename a column's name.
ALTER TABLE table
ALTER COLUMN column new_datatype; <---- This will NOT work with SQLite
This will modify a column's datatype.
ALTER TABLE table
RENAME TO new_table_name; <---- This will work with SQLite
This will modify a table's name.
PS: There are a lot of caveats with SQLite ALTER TABLE, such as:
it cannot modify a column's data type and it cannot add or remove
constraints from an existing table directly.
To alter the schema design, like modifying datatypes, we need
to follow few steps in SQLite:
1 -  we need to create a new table.
2 -  copy the data from the old table to the new table.
3 -  drop the table.
4 -  rename the new table using the old name.
Let's create some examples using python, in the users.py file.
"""
# --- CONSTRAINTS --- #
"""
Constraints are specific rules for data in a column in a table.
They can be defined when a table is created. While most of SQL database
engines support ALTER TABLE to alter the constraint, SQLite does not.
The steps to modify a constraint from a table are specified above, in
the ALTER TABLE topic.
The syntax for a constraint is as follows:
CREATE TABLE table (
    column datatype CONSTRAINT,
    column_02 datatype CONSTRAINT,
    column_03 datatype CONSTRAINT);
There are several constraints for a column, such as:
AUTOINCREMENT - Automatically increments a number for new rows added to the
table.
UNIQUE - All the values in a column are different
PRIMARY KEY - Identifies a row uniquely in a table.
FOREIGN KEY - Is a column that refers to a primary key of another table.
CHECK - Verifies if a value in a column matches a condition.
CREATE INDEX - Create indexes on a table, to speed data retrieval in
transactions.
DEFAULT - Specifies a default value for a column when a row is inserted.
To summarize: constraints define the rules that a column will have
to follow.
"""
# --- NOT NULL CONSTRAINT --- #
"""
When we talk about SQL, we have to remember that all the schemas,
views, functions, tables and so on are made to hold values.
With that in mind, we need to remind that a column contains a multitude
of values. To keep them always fulfilled, we need a constraint to do that.
The NOT NULL constraint makes a value have this behavior: enforces
a column to never accept null values. By default, a column can have
null values, and this is why it's a necessary constraint.
The syntax of the constraint is simple:
CREATE TABLE table (
column datatype NOT NULL,
column_02 datatype constraint);
In this case, we are enforcing the NOT NULL constraint
to column.
Let's see how we would do it with ALTER TABLE:
ALTER TABLE table
ALTER COLUMN column datatype NOT NULL; <---- This doesn't work with SQLite.
We've seen why this won't work with SQLite, but will work with, for example,
SQL Server database.
In MySQL, it would look like this:
ALTER TABLE table
MODIFY column datatype NOT NULL;
In the end, it's a useful constraint that manages to overwrite the default
behavior of SQL.
PS: If you try to constrain a NULL type value with a NOT NULL constraint,
the database will throw an error.
"""
# --- UNIQUE CONSTRAINT --- #
"""
To ensure that a column will only have different values in it, we have
to use the UNIQUE constraint to guarantee it.
You can have many UNIQUE constraints per table.
The syntax is as follows:
CREATE TABLE table (
column datatype NOT NULL UNIQUE,
column_02 datatype DEFAULT 'string' <---- This will work with SQLite.
);
In this case, the first column is NOT NULL and UNIQUE.
It cannot have NULL values, and all values in this column will be unique.
PS: we can also alter the constraint from a column in a table:
ALTER TABLE table
ADD UNIQUE (column); <---- This doesn't work with SQLite.
We can also drop a constraint:
ALTER TABLE table
DROP UNIQUE column; <---- This doesn't work with SQLite.
PS²: SQLite does not support adding or dropping
UNIQUE constraints via ALTER TABLE.
"""
# --- PRIMARY KEY --- #
"""
A PRIMARY KEY is used to identify a unique value in a table.
It's almost as a subset of UNIQUE. However, while we can
create multiple columns with the UNIQUE constraint, and, in a table, only
one column can be set as a PRIMARY KEY. To be fair, PRIMARY KEY
is somewhere close to a NOT NULL plus a UNIQUE constraint.
The syntax is as follows:
CREATE TABLE Persons (
    column datatype NOT NULL PRIMARY KEY,
    column_02 datatype NOT NULL,
    column_03 datatype UNIQUE,
    column_04 datatype NOT NULL
);
PS: We can also alter the constraint from a column in a table:
ALTER TABLE table
ADD PRIMARY KEY (column); <---- This doesn't work with SQLite.
Or drop the constraint:
ALTER TABLE table
DROP PRIMARY KEY column; <---- This doesn't work with SQLite.
PS²: SQLite does not support adding or dropping
PRIMARY KEY constraints via ALTER TABLE.
PS³: If you try to add a NULL value to a PRIMARY KEY the
database will throw an error.
"""
# --- FOREIGN KEY CONSTRAINT --- #
"""
A FOREIGN KEY constraint defines a value in a table that
refers to a PRIMARY KEY from another table.
A table that relates to another table, with a FOREIGN KEY,
is called a child table. The table referenced is called a parent
table.
The syntax is as follows:
CREATE TABLE Persons (
    column datatype NOT NULL PRIMARY KEY,
    column_02 datatype NOT NULL,
    column_03 datatype UNIQUE,
    column_04 datatype FOREIGN KEY REFERENCES stations(ID)
);
In SQLite it would look like this:
CREATE TABLE Persons (
    column datatype NOT NULL PRIMARY KEY,
    column_02 datatype NOT NULL,
    column_03 datatype UNIQUE,
    CONSTRAINT name <---- Giving a name to the constraint
    for good practice;
    FOREIGN KEY (column_04) <---- FOREIGN KEY name
    REFERENCES stations (ID) <---- Referenced column inside the table
    ON DELETE SET NULL <---- When parent row is deleted - optional
);
PS: Constraints are disabled by default in SQLite, so we need to set the
PRAGMA - the directive, or command to the compiler - to
PRAGMA foreign_keys = ON. This is necessary, or the FOREIGN KEY will not
work.
"""
# --- CHECK CONSTRAINT --- #
"""
A CHECK constraint is used to limit that a value can be placed in a column.
It's a CHECK condition for a column, allowing only certain values to be placed
inside a column.
The syntax is as follows:
CREATE TABLE Persons (
    column datatype NOT NULL PRIMARY KEY,
    column_02 datatype NOT NULL,
    column_03 datatype UNIQUE,
    column_04 datatype FOREIGN KEY REFERENCES stations(ID)
    CHECK (column_03 <= 30)
);
In SQLite it will look exactly like the above.
But for aesthetics purposes, we can write like this:
CREATE TABLE Persons (
    column datatype NOT NULL PRIMARY KEY,
    column_02 datatype NOT NULL,
    column_03 datatype UNIQUE CHECK (column_03 <= 30),
    column_04 datatype FOREIGN KEY REFERENCES stations(ID)
);
Or use CHECK to an entire table:
CREATE TABLE Persons (
    column datatype NOT NULL PRIMARY KEY,
    column_02 datatype NOT NULL,
    column_03 datatype UNIQUE,
    column_04 datatype FOREIGN KEY REFERENCES stations(ID),
    CHECK (COLUMN_03 <= 30 OR column_03 > column_02)
);
We can also use CHECK with the command ADD or DROP CONSTRAINT:
ALTER TABLE table
ADD CHECK (column <= 30); <---- This will not work with SQLite
and, finally, the drop syntax:
ALTER TABLE table
ADD CONSTRAINT column; <---- This will not work with SQLite
PS: Altering constrain in a table in SQLite does not work, remember it.
We need to create a new table to alter a constrain, remember:
contrary to foreign keys constraints being deactivated when using
SQLite, CHECK constraints are enforced and enabled by default,
but only when you create a table. You cannot use it ALTER TABLE with
columns. You cannot use ALTER TABLE to add or modify CHECK constraints
on columns.
"""
# --- DEFAULT CONSTRAINT --- #
"""
A DEFAULT constraint is added to set a given value for a column.
It will be added to all new fields if no value is specified.
The syntax is as follows:
CREATE TABLE Persons (
    column datatype NOT NULL PRIMARY KEY,
    column_02 datatype NOT NULL,
    column_03 datatype UNIQUE,
    column_04 datatype FOREIGN KEY REFERENCES stations(ID),
    column_05 datatype DEFAULT 'value',
    CHECK (column_03 <= 30)
);
Example (from W3Schools.com - all credits to them):
CREATE TABLE Orders (
    ID int NOT NULL,
    OrderNumber int NOT NULL,
    OrderDate date DEFAULT GETDATE()
);
Here, the DEFAULT constraint uses a function to
insert the system date automatically. No need to insert anything manually.
We can also alter a table:
ALTER TABLE table
ALTER column SET DEFAULT 'value'; <---- This will not work with SQLite
And we can drop a DEFAULT constraint from a column:
ALTER TABLE table
ALTER COLUMN column DROP DEFAULT; <---- This will not work with SQLite
PS: Remember the workaround to modify constraints in SQLite.
PS²: All syntax shown here is for SQL Server. If it doesn't work in SQLite,
I already described workarounds in previous examples.
"""
# --- INDEX CONSTRAINT --- #
"""
Before diving into this concept, we have to clarify some things:
an INDEX is not just a constraint, it's also a data structure that
is used to speed up queries. So It's an enforcer and a data structure.
It's purpose is to make data retrieval and sorting operations go faster
than it would go without it.
Remember to use indexes for columns that you query often, this will avoid
indexing columns that change frequently and will also avoid the downside
of indexes.
The syntax is as follows:
CREATE INDEX index
ON table (column);
In a real case, with SQLite, it would look like this:
CREATE INDEX idx
ON stations (municipality)
In this case, an index will be created with the idx name
for municipality in the stations table.
Think of an index like a pointer in C:
it tells the database where data is stored so searches don't scan every row.
It points to where the data is stored within a database,
so when querying, the database won't have to go through every
row until it finds a value.
We can also drop an index from a database:
DROP INDEX index; <---- This works with SQLite
In a real case it would look like this:
DROP INDEX [IF_EXISTS] idx; <---- This works with SQLite
PS: An UNIQUE INDEX would be a case where an INDEX act like a constraint.
PS²: INDEXES speed up the reading of a row, with the trade-off of slow
writes.
PS³: Because indexes are not inherently a constraint, you can manipulate them
with SQLite.
"""
# --- AUTO INCREMENT --- #
"""
The AUTO INCREMENT keyword is used in SQL to define a column that will
generate a sequence of unique values, but only when new rows are created.
It can be defined as AUTOINCREMENT - with SQLite - or AUTO_INCREMENT -
with other SQL databases.
The syntax is as follows:
CREATE TABLE table(
column_id datatype PRIMARY KEY AUTOINCREMENT - or AUTO_INCREMENT,
column_02 datatype constraint,
column_03 datatype); <---- This will work with SQLite
When we insert a value into a table with autoincrement, you don't
need to specify a value for the ID — it's automatically generated.
It will auto-increment a value by a defined amount.
So when we do this:
INSERT INTO stations (municipality, person)
VALUES ('New York','Andrew');
It will automatically add a value to the column_id with
autoincrement inside the table stations.
PS: AUTOINCREMENT is a mechanism to generate values.
So it gives the database a way to automatic generate values to
a row.
PS²: We've shown how it works in python with SQLite on the file table_01_sql.
"""
