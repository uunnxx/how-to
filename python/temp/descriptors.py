class SetName:
    def __set_name__(self, owner, name):
        print(f"{self} was named {name}")


class Foo:
    x = SetName()
    y = SetName()


# -----------------------------------------------------------------------------


class WithoutSetName:
    def __init__(self, name):
        print(f"{self} was named {name}")


class Bar:
    x = WithoutSetName('x')
    y = WithoutSetName('y')
