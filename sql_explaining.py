# --- SQL - A simple vision about it --- #
"""
SQL, or "ess cue el" - taking the example from the book -
is an acronym for Structured Query Language.
This language is used to access, manipulate and retrieve data from
a database.
Following the book:
'Databases can have one or more schemas; they give an organization
the means and the structure and contain other objects'.
When we deal with schemas, we'll deal with tables, views and functions.
Tables have fields to store data. They'll, or can have, indexes, just like
Python, or other programming languages. There are controversies that argue
about SQL pertaining to the spectrum of programming languages.
The index is part of a data structure to retrieve data from a given
data stored in an object - e.g. 3 objects inside a list, indexes [0,1,2].
Views are queries that are stored and can be instantiated in the same way
a table is.
Functions are a compilation of code that can be used to execute calculations,
other functions and can be stored and called for later usage.
A DBA - i.e. database administrator - will create those.
So, we can represent a database in this form:
-------------------------------------------|
Database ----------------------------------|
Schema --------- Inside the database ------|
Table ---------- inside the schema --------|
View  ---------- inside the schema --------|
Function ------- inside the schema --------|
-------------------------------------------|

We have four sub-languages that are used inside SQL:
DQL: Data Query Language. It's used when viewing data.
DDL: Data Definition Language. It's used to create, modify objects like views,
tables and others. DDL will be used to alter the structure of the schema,
but not its data.
DCL: Data Control Language. It's used to control the access to a given
database or its schemas; or tables, views and, or, functions.
DML: Data Manipulation Language. It's used on the data inside the tables,
views, functions. The data per se.
"""
# --- Relational, Non-Relational Databases and Transactional Databases --- #
"""
Relational databases refer to databases that stores data in tabular format with
columns and rows. The columns contain attributes and the rows have the data
values.
You can use the example of an excel spreadsheet. It has its columns with Data,
Attributes, mostly on the first row and, on the other rows, you have the data
pertained to each column.
In relational databases you are able to link tables and have connection
between a myriad of datapoints.
Non-Relational databases - NoSQL databases - are used for accessing and
managing data in a more flexible and optimized way. It normally uses other
programming languages and other types of files containing data, like json,
for applications that require models that are large, need optimization for
low latency, and have less consistency restrictions comparing to Relational
databases.
A Transactional database, whoever, is defined as a database designed to
be consistent. It either fails completely on its transaction or its
completely successful. So when a transaction fails, it maintain consistency,
which is a necessity for it to be transactional. The consistency Let's it
rollback the data, without mismatched records. So most of relational
databases are transactional.
A transactional database comes with a set of principles, for it to be
considered safe:
Atomicity: The transaction either succeeds or don't
Consistency: Data is strictly defined by a set of rules
Isolation: No transaction will interfere with another transaction
Durability: No data is lost, even with system crashes or other
set of errors occur.
With this in mind, A relational database can be transactional,
adhering to the principles of the transactional database or be more flexible.
Relational and non-relational databases relate to how one stores data;
transactional databases relate to how one deal with the operation of the data.
Some Non-relational databases can also be strict enough do adhere to the ACID
principle.
"""
# --- Data Warehouses, Data Lakes, Data Store and Data Mart --- #
"""
Data warehouse: It's a repository where multiple sources combine to store
data, making it a central point of storage. It is optimal to be used with
complex data queries and analysis. It has pre-defined schemas.
Data Lakes: It's a central repository of data where schemas are not
pre-defined. They support raw, structured, semi-structured, and unstructured
data.
Data Marts: It's a type of data warehouse, focused on a specific type of
information; that said: it's a data warehouse with more strict rules.
Data Store: It's a type of data storage system, so any database is
a data store, but not all data stores are databases.
"""
# --- Beginning working with real cases --- #
"""
Let's work with real cases.
The SELECT statements, which are queries, is a statement that declares
what data we are querying inside a database.
Let's create a python file that will create a dictionary with users
information. With that, we can create a database with sqlite3, and
use it as an example for querying.
"""
"""
We've created two files. One where we execute the code from the
table_01_sql - i.e. the file where the functions for the SQL file
is stored - and the table_01_sql.
Inside the table_01_sql we've created two functions so far:
one for creating a table inside a database, with a defined schema.
Another for inserting values to it.
"""
"""
Inside each function we can find strings defined, and meant to be sent
to the sqllite3 library - this library is written in C.
It works by compiling the SQL text statements into bytecode.
A statement consists of keywords, commands and names that are meant
to be executed by the sqllite3 library.
When we created a database, first we called the command
CREATE TABLE, followed by the name of the table.
In between parenthesis, we the code of our statement -
e.g. what we'll select. The fields inside it will define the data tables.
We can use logical data; numerical data; datetime data and much more.
The fields can be defined as a TEXT field, or an INTEGER field.
I'll try to cover lots of them in this repo.
A field is contained inside a table. Inside the users table, there
are 3 fields:
id: an INTEGER field that is also a PRIMARY KEY. The PRIMARY
KEY, in SQL is a column, or sets of columns, that are unique and
meant to be unique.
A RECORD is another name for row, being each entry that exists in a table.
All records are positioned on the horizontal axis of a table.
A column is defined by the first information on the vertical
axis. It describes the information put on a field below it.
"""
# --- Important SQL Commands --- #
"""
Here we can see important SQL commands:
CREATE TABLE - Crates a table
ALTER TABLE - Alters a table
DROP TABLE - Deletes a table
CREATE INDEX - Creates an index
DROP INDEX - Deletes an index
UPDATE - Updates data
SELECT - Extracts data
DELETE - Deletes data
INSERT INTO - Inserts new data
There are many other commands, and we'll learn them on the basics as we go on.
"""
# --- Refactoring the users file --- #
"""Let's refactor the users.py file to make it more readable.
We'll try to put every important example inside a function that,
when we need, call the SQL function, to be written.
"""
# --- Using the command SELECT --- #
"""
Now that we know a little bit more of how SQL works,
let's create a function that will send information related to the
column that we want to retrieve information.
We also need to close the database connection with the .close() method.
"""
# --- The command SELECT DISTINCT --- #
# Here we'll use a db from dataquest.io - all credits
# due to them. https://www.dataquest.io/blog/sql-basics/
# The database is an example database with fake information.
# So I'm not responsible for any given information inside given database.
# We'll only use it as an example, giving credits to them.
"""
We can use the SELECT DISTINCT, being DISTINCT another command, to
select only values that we don't want to repeat.
In this example, we'll show all municipalities inside the hubway.db,
from dataquest.io - all credits to them for the fake database -, to
show the code sample.
The structure of the statement looks like this:
SELECT DISTINCT column
FROM table;
Remember, the semicolon in the end of the statement serves as a separator.
We can also use the DISTINCT keyword inside the COUNT function.
For example: SELECT COUNT(DISTINCT column)
FROM table;
This will return the number of different municipalities
So let's refactor the function with a flag to make it
return the COUNT of different municipalities or
the name of the municipalities - True for COUNT and False
for only the name.
We'll use a default parameter as True to always return the name.
"""
# --- The WHERE clause --- #
"""
The where clause is used only to return a specified from a given column.
For example:
SELECT * FROM column
FROM table
WHERE condition
We can also use operators with the WHERE clause, like:
=; >; <; >=; <=; != or <>; BETWEEN - e.g. WHERE BETWEEN 10 AND 60 -;
LIKE - e.g WHERE condition LIKE 'q%';-; IN - e.g. IN
('Avenue')
PS: When writing text, SQL requires that you use text
in between single quotes.
Let's do a function in python that will use the WHERE clause.
"""
# --- ORDER BY keyword --- #
"""
The ORDER BY keyword can be used to order an query to sort
the returned query; it can also be in ascending or descending order.
The syntax is as follows:
SELECT column,
FROM table,
ORDER BY column ASC (ascending) / DESC (descending);
So let's make a function for to show how it works.
"""
# --- AND and OR operators --- #
"""
Operators are used with clauses to be used as conditions.
The AND operator is used to join multiple conditions and return
a result if both are true.
Example:
SELECT *
FROM stations
WHERE municipality = 'Boston' and municipality = 'Cambridge'
The OR operator is used to join multiple conditions and return
a result if one of the conditions is true.
Example:
SELECT *
FROM stations
WHERE municipality = 'Boston' or municipality = 'Cambridge'
If we use the first in our table, it will return no results
from the query.
If we use the latter, we will return all tuples with data
from the Boston and Cambridge municipalities.
"""
