import sqlite3 as sql


connections = sql.connect('users.db')
cursor = connections.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users
    (user_id INT, first_name TEXT, last_name TEXT, email_address TEXT)
    """)

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Users
#     (user_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, email_address TEXT)
#     """)

# cursor.execute("INSERT INTO Users VALUES ('Taxi Driver', 'Martin Scorsses', 1976)")
# cursor.execute("SELECT * FROM Movies")


# users_list = [
#     (1, 'David', 'Johnson', 'david_johnson@gmail.com'),
#     (2, 'Mary', 'Black', 'mary25523@gmail.com'),
#     (3, 'George', 'Peaterson', 'son@gmail.com'),
#     (4, 'John', 'Doe', 'john_doe@gmail.com'),
#     (5, 'Tom', 'Adlov', 'tom@gmail.com'),
# ]


# cursor.executemany(
#     """INSERT INTO Users(
#         user_id,
#         first_name,
#         last_name,
#         email_address
#     ) VALUES (?, ?, ?, ?)""", users_list)


cursor.execute("SELECT * FROM Users")
# print(cursor.fetchall())

res = cursor.execute("SELECT * FROM Users WHERE user_id=?", (1,))
print(res.fetchone())


email_addresses = cursor.execute("SELECT email_address FROM Users")
print(email_addresses.fetchall())
# connections.commit()

connections.close()
