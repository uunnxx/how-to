def br():
    print(f"\n{'-' * 80}\n")


class A():
    def dothis(self):
        print('doing this in A')


class B(A):
    pass


class C(A):
    def dothis(self):
        print('do this in C')


class D(B, C):
    pass


d_instance = D()
d_instance.dothis()

print(D.mro())


br()


class Logger():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._logger


obj = Logger()
obj2 = Logger()
print(obj == obj2)
