from pandas import Series
from scipy.stats import entropy
from random import randbytes


def calc_entropy(data):
    s = Series(data)
    counts = s.value_counts()
    return entropy(counts)


min_len = 5


def field_entropy(v):
    if type(v) in (str, bytes, bytearray):
        if type(v) is str:
            b = bytearray(v, 'utf-8')
        else:
            b = bytearray(v)
        if len(b) >= min_len:
            e = calc_entropy(b)
            return e
        else:
            return None
    else:
        return None


text = 'Hello world!'
text2 = 'hello world'

print(f"{text} Entropy: {field_entropy(text)}")
print(f"{text2} Entropy: {field_entropy(text2)}")


r = randbytes(12)
r2 = randbytes(11)

print(f"{r} Entropy: {field_entropy(r)}")
print(f"{r2} Entropy: {field_entropy(r2)}")
