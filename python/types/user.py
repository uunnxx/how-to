from datetime import datetime
from dataclasses import dataclass


@dataclass
class User:
    birthday: datetime


users = (
    User(birthday=datetime.fromisoformat("1998-01-01")),
    User(birthday=datetime.fromisoformat("1985-07-29")),
    User(birthday=datetime.fromisoformat("2000-10-10"))
)


def get_younger_user(users: list[User]) -> User:
    sorted_users = sorted(users, key=lambda x: x.birthday)
    return sorted_users[0]


print(get_younger_user(users))



