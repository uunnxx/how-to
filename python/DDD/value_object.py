from dataclasses import dataclass


@dataclass(frozen=True)
class StreetAddress:
    '''Represents a street address.'''
    street: str
    city: str
