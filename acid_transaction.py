import sqlite3
import sys

# Here we'll establish a connection with out db.
connection = sqlite3.connect('acid_demo.db')

# Here we'll create the cursor object
cursor = connection.cursor()

# Let's say we want to transfer money from Alice, inside the DB,
# To Bob, also inside the db.
# We need it to be a transaction, a single transaction that cannot
# be overwrite and will be protected.


# Let's create a function to transfer money from Alice to Bob.
def transfer(sender, receiver, amount):
    # We need to maintain consistency, with a rollback. For
    # that, we need a try-except block.
    try:
        connection.execute("BEGIN TRANSACTION;")
        # This is needed to show that we're beginning a transaction.
        # It's redundant, but necessary to show how it works.

        # We need to verify if the sender exists:
        # We also need to verify if the sender has the amount
        cursor.execute('SELECT balance '
                       'FROM accounts '
                       'WHERE id = ?;', (sender,))
        row = cursor.fetchone()

        # We need to verify if the sender exists:
        if row is None:
            print("There's no account with this id. \n")
            connection.rollback()
            sys.exit()

        row = int(row[0])
        if amount > row:
            print("Amount exceeds 1000 dollars. \n")
            connection.rollback()
            sys.exit()

        else:
            sentence_sender = 'UPDATE accounts ' \
                            'SET balance = balance - ? ' \
                            'WHERE id = ?;'
            cursor.execute(sentence_sender, (amount, sender))
            # Here we are parameterizing the query, to ensure
            # the sentence is send literally and interpreted
            # literally by the db.

            receiver_amount = 'UPDATE accounts ' \
                              'SET balance = balance + ? ' \
                              'WHERE id = ?;'

            cursor.execute(receiver_amount, (amount, receiver))
            # If both transactions are successful, we commit them.
        connection.commit()
    except Exception as e:
        # If any errors occur during the transaction,
        # we'll rollback the transaction. This is to ensure
        # security.
        connection.rollback()
        print(f'Transaction failed because of the following error {e}')


# Now let's print the balance from each account before every transfer:
print('Balances before transaction: \n')
cursor.execute('SELECT owner, balance '
               'FROM accounts;')
row = cursor.fetchall()
for i in row:
    print(*i, "\n")

# Let's perform the transaction
transfer(1, 2, 600)

# Now let's print the balance from each account after every transfer:
print('Balances after transaction: \n')
cursor.execute('SELECT owner, balance '
               'FROM accounts;')
row = cursor.fetchall()
for i in row:
    print(*i, "\n")

# Let's close the connection for both the cursor and the connection:
cursor.close()
connection.close()

# With this, we exemplify ACID + Transaction
