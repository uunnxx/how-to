from contextlib import suppress



def code():
    pass

try:
    pass
except ValueError:
    pass
except EOFError:
    pass



try:
    code()
except (ValueError, EOFError):
    pass


with contextlib.suppress(ValueError, EOFError):
    code()



