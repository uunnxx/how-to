from my_module import say_hi, __version__

# from my_module import *
# This will import all public names such as `say_hi` but would not import __version__ because
# it starts with double underscores.

# WARNING: Remember that you should avoid using import-star, i.e. from my_module import *
# Zen of Python:
# One of Python's guiding principles is that "Explicit is better that Implicit".
# Run `import this` in Python to learn more.


say_hi()
print('Version', __version__)
