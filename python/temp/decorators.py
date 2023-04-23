import functools  # Part of Python standard library


def decorator(wrapped_function):
    def _wrapper(*args, **kwargs):
        # do something before the function call
        result = wrapped_function(*args, **kwargs)
        # do something after the function call
        return result
    return _wrapper

# decorator with functools.wraps added
def decorator_with_wraps(wrapped_function):
    @functools.wraps(wrapped_function)
    def _wrapper(*args, **kwargs):
        # do something before the function call
        result = wrapped_function(*args, **kwargs)
        # do something after the function call
        return result
    return _wrapper

import wrapt  # Requires installing the 'wrapt' library

# decorator powered by wrapt
@wrapt.decorator
def decorator_with_wrapt(wrapped_function, instance, args, kwargs):
    # do something before the function call
    result = wrapped_function(*args, **kwargs)
    # do something after the function call
    return result

def test_decorators():

    @decorator
    def func1():
        return 'I'

    @decorator_with_wraps
    def func2():
        return 'code'

    @decorator_with_wrapt
    def func3():
        return 'python'

    assert func1() == 'I'
    assert func2() == 'code'
    assert func3() == 'python'

