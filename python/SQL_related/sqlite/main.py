import sqlite3 as sql


connection = sql.connect('db.sqllite3')

query = connection.cursor()


query.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name VARCHAR,
        password VARCHAR)
""")

connection.commit()


while True:
    name = input('Name: ')

    if not name:
        break

    password = input('Password: ')



    query.execute("INSERT INTO user(name, password) VALUES (?, ?)", (name, password))
    connection.commit()

print('\nUsers:\n')

query.execute("SELECT * FROM user")

# user_row = query.fetchone()
users_row = query.fetchall()


# print(user_row)

for user in users_row:
    print(user)


# Close
query.close()
connection.close()
