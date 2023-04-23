import sqlite3 as sql


connections = sql.connect('movies.db')
cursor = connections.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Movies
#     (Title TEXT, Director TEXT, Year INT)
#     """)

# cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsses', 1976)")
# cursor.execute("SELECT * FROM Movies")


# famous_films = [
#     ('Pulp Fiction', 'Quentin Tarantino', 1994),
#     ('Back to the Future', 'Steven Spielberg', 1985),
#     ('Moonrise Kingdom', 'Wes Anderson', 2012)
# ]
#
#
# cursor.executemany("INSERT INTO Movies VALUES (?, ?, ?)", famous_films)

# cursor.execute("SELECT * FROM Movies")
# print(cursor.fetchall())

release_year = (1985, )
cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)
print(cursor.fetchall())

connections.commit()
connections.close()



