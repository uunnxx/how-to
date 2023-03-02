def log_return(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        print(res)
        return res
    return wrapper

@log_return
def f(*args, **kwargs):
    return args, kwargs

f(1, 2, 3, a=4, b=5)
f((1, 2, 3), {'a': 4, 'b': 5})
f((1, 2, 3), {'a': 4, 'b': 5})
