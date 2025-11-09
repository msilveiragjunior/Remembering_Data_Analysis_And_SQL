import table_01_sql
# --- Beginning SQL with Python --- #
# Creating an empty dictionary to create a table for it
table_01 = {
}

number_of_users = input("Insert the number of users: \n")
numbers_of_keys = input("Please, specify the number of keys inside each "
                        "user: \n")
for x in range(0, int(number_of_users)):
    for i in range(0, int(numbers_of_keys)):
        key = input("Insira o nome da chave: \n")
        table_01[key] = input("Insira um valor para a chave: \n")
print(table_01)
