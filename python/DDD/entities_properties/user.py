from enum import Enum


class AbstractEntity:
    pass


class UserRole(Enum):
    OWNER = 'owner'
    ADMINISTRATION = 'administration'
    MEMBER = 'member'


class User(AbstractEntity):
    def __init__(
        self,
        tenant_id: str,
        user_id: str | None,
        name: str | None,
        role: UserRole.MEMBER
    ) -> None:
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.name = name
        self.role = role

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(other, User):
            return False
        return (
            self.tenant_id == other.tenant_id and
            self.user_id == other.user_id
        )



# def main():
#     a = True
#     b = True
#     c = True
#     d = True
#
#     return (
#         a == b and \
#         c == d
#     )
#
#
# print(main())
