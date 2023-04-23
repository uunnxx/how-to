import enum
class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


print(f"Member name: {BugStatus.wont_fix.name}")
# 'Member name: wont_fix'
print(f"Member name: {BugStatus.wont_fix.value}")
# 'Member name: 4'
print(f"Member name: {BugStatus.wont_fix.value}")
# 'Member name: 4'


for status in BugStatus:
    print(f"{status.name:15} = {status.value}")


# print(BugStatus.)

print(BugStatus.wont_fix.name)
print(BugStatus.wont_fix.value)

print('-' * 80)

class SomeClass:
    def __init__(self):
        self._some_dict: dict[str, int] = {}

    def some_method(self):
        self._some_dict['some_key'] = 123
        self._some_dict[123] = 'some_key'


a = SomeClass()
a.some_method()
print(a._some_dict)
