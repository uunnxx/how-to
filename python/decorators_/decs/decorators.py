import functools
import time


def do_twice(func):
    def wrapper():
        func()
        func()

    return wrapper


def do_twice_with_one_arg(func):
    def wrapper(one_arg):
        func(one_arg)
        func(one_arg)

    return wrapper


def do_twice_with_args(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


def do_twice_with_args_and_return(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


def do_once(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        value = func(*args, **kwargs)

        return value

    return wrapper_decorator


def timer(func):
    """Print teh runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        print('Started measuring the function')
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Finished {func.__name__!r} in {end - start:.4f} seconds')

        return value

    return wrapper_timer



def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}= {v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')

        value = func(*args, **kwargs)

        print(f'{func.__name__!r} returned {value!r}')

        return value

    return wrapper_debug


def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down


PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func
