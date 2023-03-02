# 1.1 Classes
# From the OOP perspective, classes describe objects, and each object is
# an instance fo a class. The `class` statement allow us to define a class.
# For convention, we name classes using
# `CamelCase` and methods using `snake_case`.

# create_apartment.py

class Appartment:
    '''
    Class that represents an apartment for sale value is in USD
    '''
    def __init__(self, _id, mts2, value):
        self._id = _id
        self.mts2 = mts2
        self.value = value
        self.sold = False

    def sell(self):
        if not self.sold:
            self.sold = True
        else:
            print('Appartment {} was sold'.format(self._id))


# To create an `object`, we must create an instance of a class, for example, to create
# an apartment for sale we have to call the class `Apartment` with the necessary
# parameters to initialize it:

# instance_apartment.py

from create_apartment import Apartment

d1 = Apartment(_id=1, mts2=100, value=5000)

print('sold?', d1.sold)
d1.sell()

print('sold?', d1.sold)
d1.sell()

# sold? False
# sold? True
# Apartment 1 was sold

# We can see that the __init__ method initialize the instance by setting the attributes (or date)
# to the initial values, passed as arguments. The first argument in the `__init__`
# method is `self`, which corresponds to the instance itself.
