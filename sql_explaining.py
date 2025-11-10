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
e.g. what we'll select. Re
"""
