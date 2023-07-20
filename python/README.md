# How-To Python


## Dunders
```
# Operation             # Method

a < b                 # a.__lt__(b)
a > b                 # a.__gt__(b)
# ...
repr(a)               # a.__repr__()
a.b                   # a.__getattribute__(b)
a(b)                  # a.__call__(b)

~a                    # a.__invert__(self)
+a                    # a.__pos__(self)
-a                    # a.__neg__(self)

a + b                 # a.__add__(b)
b + a                 # a.__radd__(self, b)
a += b                # a.__iadd__(self, b)

a - b                 # a.__sub__(self, b)
b - a                 # a.__rsub__(self, b)
a -= b                # a.__isub__(self, b)

a * b                 # a.__mul__(self, b)
b * a                 # a.__rmul__(self, b)
a *= b                # a.__imul__(self, b)

a // b                # a.__floordiv__(self, b)
b // a                # a.__rfloordiv(self, b)
a //= b               # a.__ifloordiv__(self, b)

a / b                 # a.__truediv__(self, b)
b / a                 # a.__rtruediv__(self, b)
a /= b                # a.__itruediv__(self, b)

a ** b                # a.__pow__(self, b)
b ** a                # a.__rpow__(self, b)
a **= b               # a.__ipow__(self, b)

a & b                 # a.__and__(self, b)
b & a                 # a.__radd__(self, b)
a &= b                # a.__iand__(self, b)

a << b                # a.__lshift__(self, b)
b << a                # a.__rlshift__(self, b)
a <<= b               # a.__ilshift__(self, b)

a >> b                # a.__rshift__(self, b)
b >> a                # a.__rrshift__(self, b)
a >>= b               # a.__irshift__(self, b)

a | b                 # a.__or__(self, b)
b | a                 # a.__ror__(self, b)
a |= b                # a.__ior__(self, b)

a ^ b                 # a.__xor__(self, b)
b ^ a                 # a.__rxor__(self, b)
a ^= b                # a.__ixor__(self, b)

a @ b                 # a.__matmul__(self, b)
b @ a                 # a.__rmatmul__(self, b)
a @= b                # a.__imatmul__(self, b)

a % b                 # a.__mod__(self, b)
b % a                 # a.__rmod__(self, b)
a %= b                # a.__imod__(self, b)

divmod(a, b)          # a.__divmod__(self, b)
divmod(b, a)          # a.__rdivmod__(self, b)
abs(a)                # a.__abs__(self)
operator.index(a)     # a.__index__(self)
complex(a)            # a.__complex__(self)

floot(a)              # a.__float__(self)
int(a)                # a.__int__(self)

ceil(a)               # a.__ceil__(self)
floor(a)              # a.__floor__(self)
round(a)              # a.__round__(self)
trunc(a)              # a.__trunc__(self
```
