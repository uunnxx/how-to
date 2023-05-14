import weakref


def br():
    print(f"\n{'-' * 80}\n")


class ExpensiveObject:
    def __del__(self):
        print(f'(Deleting {self})')


obj = ExpensiveObject()
r = weakref.ref(obj)

br()

print('obj:', obj)
print('ref:', r)
print('r():', r())

br()

print('deleting obj')

br()

del obj

br()
print('r():', r())
