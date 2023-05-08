class DataDescriptor:
    def __get__(self, instance, owner):
        print(f"DataDescriptor.__get__({self!r}, {instance!r}, {owner!r})")

    def __set__(self, instance, value):
        print(f"DataDescriptor.__get__({self!r}, {instance!r}, {value!r})")


class NonDataDescriptor:
    def __get__(self, instance, owner):
        print(f"NonDataDescriptor.__get__({self!r}, {instance!r}, {owner!r})")


class Owner:
    a = DataDescriptor()
    b = NonDataDescriptor()
