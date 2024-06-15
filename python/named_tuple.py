from collections import namedtuple
from typing import NamedTuple


# Result = namedtuple('Result', 'status address wallet_type balance')
# Result = namedtuple('Result', ['status', 'address', 'wallet_type', 'balance'])


class Result(NamedTuple):
    status: str = 'err'
    address: str = ''
    wallet_type: str = 'v1'
    balance: int = 0

    @property
    def active_balance(self):
        return (self.balance > 0)




result = Result('ok', 'address_atsehsaton', 'v1', 4275)

print(result.status)
print(result.address)
print(result.wallet_type)
print(result.balance)


print(result.active_balance)
