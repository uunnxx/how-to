from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'Jane Doe'


# user = User(id='123')
# user_x = User(id='123.45')
user = User(id=123)
user_x = User(id=123.45)  # Auto-casting to int (https://docs.pydantic.dev/usage/models/#data-conversion)


print(user_x)

# assert user.id == 123
# assert user_x.id == 123
# assert isinstance(user_x.id, int)
