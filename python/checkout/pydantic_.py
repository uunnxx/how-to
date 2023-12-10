from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int


user_data = {
    'name': 'Jack',
    'email': 'jack@example.com',
    'account_id': 121212
}


user = User(**user_data)

print(user)
print()
print(user.name)
print(user.email)
print(user.account_id)
