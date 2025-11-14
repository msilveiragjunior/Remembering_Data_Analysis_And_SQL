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
A Transactional database, however, is defined as a database designed to
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
# --- AND, OR and NOT operators --- #
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
The NOT operator is used with other operators
with clauses to negate the condition given
For example:
SELECT *
FROM stations
WHERE NOT municipality = 'Boston'
In this example, we select all rows where the municipality
is not Boston. We use the NOT operator with the equal operator.
SELECT *
FROM stations
WHERE municipality NOT IN ('Boston', 'Cambridge')
Here we use the NOT operator with the IN operator, that
we'll take a look later.
In this, we'll query and return all the rows
that are not in boston or cambridge
"""
# --- Null Values --- #
"""
A null value is a field without a value.
A NULL value field differs from a zero value field. For Example:
You can count a 0 value field, it contains nothing, but it's a value.
A NULL value field is a field without a field: the absence of value.
The syntax of creating a field with NULL values is the following:
CREATE TABLE users (
id INTEGER PRIMARY KEY,
username TEXT,
emaiL TEXT NULL) <----- This is defined as an optional field
To create a table with a field that is mandatory, we add the NOT
NULL constraint.
CREATE TABLE users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL, <------- This field is NOT optional
emaiL TEXT NULL)
Testing if a value is NULL or NOT NULL cannot be done with comparison
operators.
We have to use the IS NULL or IS NOT NULL operators.
The syntax is as follows:
SELECT column
FROM table
WHERE column IS NULL
This will return all values with empty fields.
PS:
There's much debate on either NULL is a value or a marker.
Let's leave this debate for another time.
We'll create a function, this time, to see how many fields are null
and how many are not.
"""
# --- UPDATE statement --- #
"""
The UPDATE statement is very simple and need no examples in code.
This statement is used to update a column with a new value, or columns
with new values.
The syntax is as follows:
UPDATE table
SET column_01 = value_01, column_02 = value_02, column_03 = value_03
WHERE condition
For example:
UPDATE stations
SET municipality = 'New York'
WHERE municipality = 'Boston'
This will update all the fields where Boston is written to New York.
PS:
If there's no WHERE clause in the query, all the names
from municipality, from the example, will be updated to NeW York.
"""
# --- DELETE statement --- #
"""
The Delete statement is also very simple.
It deletes a record in a table given a condition.
If there's no condition, then all the records
from the table will be deleted.
The syntax is as follows:
DELETE FROM table
WHERE Condition
For example:
DELETE FROM stations
WHERE municipality = 'Boston'
This code deletes all rows with Boston in it.
We can make is more strict, to delete only one row,
by defining a more specific characteristic from the field.
To delete a table, we can use the DROP TABLE statement
For example:
DROP TABLE stations
This will delete the table stations completely. Not only
remove its fields, but delete the table itself.
"""
# --- SELECT TOP clause --- #
"""
The SELECT TOP clause is also another simple clause.
It's used to specify the number of records to query
from the statement.
The syntax vary, but we'll use the SQL Server syntax for the
purpose of giving an example:
SELECT column,
FROM table,
WHERE condition,
LIMIT number;
For example, if we want to limit the number the
5 first records of the query, we'll write the statement
like this:
SELECT *
FROM stations
WHERE municipality = 'Cambridge'
LIMIT 5;
This would return the first 5 rows with the municipality of Cambridge
Without the WHERE clause, this would return the first 5 rows of
the table.
If you want to sort the result, we can also add a ORDER BY keyword
to the statement
It would look like this:
SELECT *
FROM stations
WHERE municipality = 'Cambridge'
ORDER BY station ASC
LIMIT 5;
This would order in ascending order.
Or if you want to order it alphabetically:
SELECT *
FROM stations
WHERE municipality = 'Cambridge'
ORDER BY station
LIMIT 5;
"""
# --- Aggregate Functions --- #
# --- Min and Max --- #
"""
The min() function queries all the smallest values from
a column and returns it.
The max() function does the opposite.
The syntax is as follows:
SELECT min(column)
FROM table
WHERE condition;
So if we were to use it with a TEXT, it would return
the first one in alphabetical order.
If we were to use it a INTEGER column, it would
return the smallest number.
We can also use GROUP BY with these functions,
We could group them by another column.
For example
SELECT min(lat), municipality
FROM stations
GROUP BY municipality
It would return the min value for each municipality
"""
# --- COUNT() --- #
"""
The count() function gives us the result of a query
from a table.
The syntax is as follows:
SELECT COUNT(column)
FROM table
WHERE condition;
For example:
SELECT COUNT(municipality)
FROM stations
This would query the number 142 and return it.
This is the number of entries inside the database.
We can also add a WHERE clause:
SELECT COUNT(municipality)
FROM stations
WHERE municipality = 'Cambridge'
This would return the number of entries
where cambridge is written.
We can use all the other clauses and from the examples above.
"""
# --- SUM() --- #
"""
To return the sum of a numeric column we we'll use the
sum() function.
The Syntax of the function is as follows:
SELECT sum(column)
FROM table
WHERE condition;
So if we were to sum the lat of a station, we would do:
SELECT sum(lat)
FROM stations
WHERE lat > 40
This would not be useful, but would return the sum of all
latitudes above 40 inside the table stations.
We can also use expressions inside the sum function:
SELECT sum(lat / 10)
FROM stations
WHERE lat > 40
This would return the number 600. Give or take.
"""
# --- AVG() --- #
"""
This function returns the average value of all the numbers
in a numeric column.
The syntax is as follows:
SELECT AVG(column)
FROM table
WHERE condition;
So if we were applying it to the lat column, as before,
it would appear like this:
SELECT avg(lat)
FROM stations
WHERE lat > 40
And the return would be something like 42.3...
We can also take out the WHERE clause and
just take the average of all latitudes:
SELECT avg(lat)
FROM stations
We can also use a sub-query to query an expression:
SELECT *
FROM stations
WHERE lat > (
SELECT avg(lat)
FROM stations);
(This example is from the w3schools.com site, so credits due
to them for the logic of the example.)
This will return all the lats that are
higher than the average of all lats.
"""
# --- Like Operator --- #
"""
With the LIKE operator we'll implement functions to try
to explain it better. It's a deceptive operator.
Just a out of place PS:
We are implementing non parameterized examples, but this
opens doors to cyber security problems. It's better to write
something like a fixed sentence than to send parameters to a function
that can accept any type of format.
Non-parameterized sentences open doors to sql injections.
So while I'm giving examples on how to do it, I also
know that it's not the best practice. However, the purpose
of this repo is to remember and remind me of central aspects
of the language and the junction of SQL and Python. All while, after
the basics, doing analysis.
So let's continue:
The LIKE operator works in conjunction with the WHERE clause. It's
used to query a specific pattern inside a column.
We often use wildcards with the LIKE operator.
Here I'm following the order of the w3schools - so rights for the
order of the structure of knowledge to them. So we'll analyze wildcards,
in depth, later.
The syntax for the LIKE operator looks simple:
SELECT column
FROM table
WHERE column LIKE condition;
So if we were to apply it to a real case, it would look like this:
SELECT *
FROM stations
WHERE municipality LIKE 'c%' - remember, SQLITE is not case sensitive.
We can also use the logic operators with LIKE.
We can build statements that uses the wildcard '%something%' to
look for a sentence that contains the word something, in this case.
We can combine wildcards or go without then. It's your choice.
So let's code the function to see the query.
"""
# --- Wildcards --- #
"""
Wildcards are used with the LIKE operator to substitute
characters in a string.
While the LIKE operator precedes these wildcards; the LIKE
operator, itself, is used with the WHERE clause to query
patterns or collections of patterns in a column.
The Wildcard characters are used with in between apostrophes,
for example
Where column LIKE 'a%' <---- this tells the database to query all
fields beginning with the letter a - this is not case sensitive
when dealing with sqllite.
Here we can give examples of what are the wildcard characters available
%: This represents a sequence of characters - zero or more. If the character
comes before the percentage symbol, then the sql query will check for
fields beginning with a certain character - UTF-8 usually.
When the character, or sequence of characters comes after the symbol,
then it will check the last character of a field - or the sequence of
characters.
When we use a letter in between two percentage symbols, it checks
for the letter anywhere on the string.
_ : The underscore character, itself, represents any single character.
For example:
'L_nd_n' <--- can be represented by any given character listed in a field;
that is, one that matches the pattern. London would be a matching pattern,
or Landen. And so on. Due to our use of vowels and consonants, usually it'll
be filled is a vowel. At least with this pattern. We can also use two
underscores, to match a pattern with two unknown characters.
[] : The brackets represents any single character inside the brackets.
With that, I mean that any character, even when not separated by commas,
will be taken into account when defining the pattern.
For example:
Where table LIKE '[abc]%' joins the % wildcard with the [] wildcard,
making it query for any field beginning with either a,b or c letter.
While '%[abc]' will query for any field ending with these characters.
We can use the wildcard hyphen '-' symbol to give a spectrum of letters as
a pattern, for example:
'[a-d]%' will query all the fields beginning with the letters a, b, c and d.
This is really useful when dealing with patterns that are continuous. At
least with the characters.
We can combine wildcards as we seen fit.
^: The carat operator does not work with SQLite, the one that we are using.
So instead of using the LIKE, we should use the GLOB operator. With the glob
operator, we should use the symbol ! for negation.
For example:
GLOB '[!a]*' Would check if the first character is NOT a,
then would check any other characters after that and accept it.
So, when using SQLite, we need to remember this:"
brackets and carats do not work. We need GLOB expressions or
REGEX, for complex expressions for it to work. We need to use then
instead of the LIKE operator.
And, as a PS:
if no wildcard is defined. The exact match of a string will be queried.
"""
# --- In Operator --- #
"""
The IN operator works as way to define multiple values with the WHERE
clause, allowing you to query multiple strings.
The syntax is simple:
SELECT column
FROM table
WHERE column IN (value);
If we were to use in a real situation, it would look like this:
SELECT municipality
FROM stations
WHERE municipality IN ('Cambridge', 'Boston')
It would return all the rows that have Cambridge
and Boston in their municipality column.
We can use the NOT keyword in front of the operator
to negate all the values inside the list.
We can also, in the real world, use a sub-query.
For example:
SELECT municipality
FROM stations
WHERE lat IN (SELECT lat FROM stations WHERE lat > 42.35)
PS: It's simpler to write WHERE lat > 42.35,
but for the sake of the explanation. I'm doing it in a convoluted
way to show how IN works with sub-queries.
Let's dive it in a pythonic way making a function to show it
working.
"""
# --- BETWEEN Operator --- #
"""
When working with ranges we cannot forget about the BETWEEN
operator. It works by querying the values between a range
that is defined by the programmer. It can be used with numbers,
text and or dates.
The syntax is simple:
SELECT column
FROM table
WHERE column BETWEEN value_01 AND value_02;
If we were to give an real life example:
SELECT lat
FROM stations
WHERE lat BETWEEN 42.3 and 42.7;
We can also use it text:
SELECT municipality
FROM stations
WHERE municipality BETWEEN 'Boston' and 'Denver';
This will return all values between Boston and Denver
Or with dates:
SELECT municipality
FROM stations
WHERE municipality BETWEEN '2005-07-01' and '2007-07-01';
This will return all values between July 01 of 2005 and
July 01 of 2007
PS: BETWEEN is inclusive for both endpoints. So it will show
everything from Boston and Denver with both included, in this
example, in particular. The others will follow the same logic.
"""
# --- Aliases --- #
"""
When given a table or a column, we may choose not to use their
real names. We can do that to make our tables, or a column,
more approachable. Facilitating reading and simplifying queries.
To do that we will use the AS keyword. These aliases only exist
for the duration of a specific query. The syntax is as follows:
SELECT column AS alias
FROM table
In a real case, it would look like this:
SELECT municipality AS city
FROM stations
The same syntax applies to a table.
We can choose to add two or more aliases. To do that, we
only need a comma after the first alias is set.
To add spaces, or create a sentence as an alias, we need
the use of brackets. For example:
SELECT municipality AS [A city inside the United States]
FROM stations
PS: that alias was convoluted haha
We can also use double quotes instead of brackets.
We can choose to concatenate columns. To do that,
we will use this syntax:
SELECT Column_1 || ', ' || Column_02 AS Something
FROM table
A real example using the two possibilities above would
be this:
SELECT municipality || ', ' || lat AS ['City and Lat']
FROM stations
This query would return the municipality, followed by a
comma and a space, then followed by the latitude.
'City and Lat'
Cambridge, 42.356543...
We would combine columns and change their aliases.
If you don't want the apostrophe on the column name, then the
code would be this:
SELECT municipality || ', ' || lat AS [City and Lat]
FROM stations
However, they - brackets or quotes - are necessary to include special
characters - e.g. spaces, accents, punctuation and so on - in your alias.
We can also give an alias to a table. It's useful when used
with multiple tables.
For example:
SELECT a.Column_01, a.Column_02
FROM table_01 AS a, table_02 AS b
WHERE a.Column_01 = 'Something' AND a.Column_02 = b.Column_02
This would return all the records where a.Column_02 equals
to b.Column_02, and both have these columns, AND where a.Column_01
have a value of 'Something'
So, to summarize:
Aliases should be used for readability when functions are in use;
there is more than and one table in a query; when we want to combine columns,
and for readability.
"""
