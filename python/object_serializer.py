import pickle
import json
from datetime import datetime


simple = dict(
    list=[1, 2, 3],
    text='string',
    number=3.44,
    boolean=True,
    none=None
)


# -----------------------------------------------------------------------------


class A(object):
    def __init__(self, simple):
        self.simple = simple

    def __eq__(self, other):
        if not hasattr(other, 'simple'):
            return False

        return self.simple == other.simple

    def __ne__(self, other):
        if not hasattr(other, 'simple'):
            return True

        return self.simple != other.simple


complex_b = dict(a=A(simple), when=datetime(2016, 3, 7))


# print(pickle.dumps(simple))

# print(pickle.dumps(complex_b))


# pickle.dump(complex_b, open('complex.pkl', 'wb'))

# print(json.dumps(simple))
# print(json.dumps(simple, indent=4))
print(json.dumps(complex_b, indent=4))

