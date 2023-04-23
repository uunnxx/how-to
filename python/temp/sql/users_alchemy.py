import sqlalchemy as db


engine = db.create_engine('sqlite:///users-alchemy.db')
metadata = db.MetaData()
connection = engine.connect()

users = db.Table(
    'Users', metadata,
    db.Column('user_id', db.Integer, primary_key=True),
    db.Column('first_name', db.Text),
    db.Column('last_name', db.Text),
    db.Column('email_addresses', db.Text)
)

metadata.create_all(engine)


insertion_query = users.insert().values([
    {'first_name': 'David', 'last_name': 'Johnson', 'email_addresses': 'david_johnson@gmail.com'},
    {'first_name': 'Mary', 'last_name': 'Black', 'email_addresses': 'mary25523@gmail.com'},
    {'first_name': 'George', 'last_name': 'Peaterson', 'email_addresses': 'son@gmail.com'},
    {'first_name': 'John', 'last_name': 'Doe', 'email_addresses': 'john_doe@gmail.com'},
    {'first_name': 'Tom', 'last_name': 'Adlov', 'email_addresses': 'tom@gmail.com'},
])


connection.execute(insertion_query)

selection_query = db.select([users.columns.email_addresses])
selection_result = connection.execute(selection_query)

print(selection_result.fetchall())
