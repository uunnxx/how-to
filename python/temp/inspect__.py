import inspect
import types
from typing import cast


def foo():
    print(cast(types.FrameType, inspect.currentframe()).f_code.co_name)


foo()
