from dataclasses import dataclass


Phone = str


@dataclass
class User:
    user_id: int
    phone: Phone


def get_user_phone(user: User) -> Phone:
    return user.phone
