from loguru import logger
import sys


# logger.add(stderr, format="{time} {level} {message}", filter="", level="INFO")
# logger.add(stderr, format="{level} {message}", filter="", level="INFO")
logger.remove()
logger.add(sys.stdout, colorize=True, format="<yellow>{time:YYYY-MM-DD at HH:mm:ss}</yellow> | <magenta>{level}</magenta> | <level>{message}</level>")


def br():
    print(f"\n{'-' * 80}\n")


def wrong_user_display(user_metadata: dict = {"name": "John", "age": 30}) -> str:
    name: str = user_metadata.pop("name")
    age: int = user_metadata.pop("age")

    # logger.debug(f"{name=} {age=}")

    return f"{name} ({age})"


wrong_user_display()
# print(wrong_user_display({"name": "Jane", "age": 20}))
# print(wrong_user_display())


br()


def user_display(user_metadata: dict = None) -> str:
    user_metadata: dict = user_metadata or {"name": "John", "age": 30}
    name: str = user_metadata.pop("name")
    age: int = user_metadata.pop("age")

    logger.debug(f"{name=} {age=}")

    return f"{name} ({age})"


user_display()
user_display({"name": "Jane", "age": 20})
user_display()


br()


class BadList(list):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"

        return f"[{prefix}] -> {value}"


b1 = BadList((0, 1, 2, 3, 4, 5))
print(b1[0])
print(b1[1])
print(b1[2])
print(b1[3])
print(b1[4])
# print(''.join(b1))  # TypeError: sequence item 0: expected str instance, int found


br()


from collections import UserList


class GoodList(UserList):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        return f"[{prefix}] --> {value}"


g1 = GoodList((0, 1, 2, 3, 4, 5))
print(g1[0])
print("; ".join(g1))


br()


logger.remove()
logger.add(sys.stdout, backtrace=True, diagnose=True)  # Caution, may leak sensitive data in prod

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")


nested(0)
