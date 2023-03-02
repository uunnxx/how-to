import os
import sys
import inspect


# print(__file__)
# print(sys.argv[0])
# print(os.path.basename(__file__))


print()
# print(inspect.stack())
# print(type(inspect.stack()))

# print()

for i in inspect.stack()[0]:
    print(i)

# a = inspect.stack()
#
# print()
# print(a[1][0])
