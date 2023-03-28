def log_function_call(original_function):
    def wrapper_function(*args, **kwargs):
        result = original_function(*args, **kwargs)
        print(f"Calling function \n{original_function.__name__}:"
              f"\n\t>> args: {args}"
              f"\n\t>> kwargs: {kwargs}"
              f"\n\t>> result: {result}")
        return result
    return wrapper_function


@log_function_call
def add_numbers(x, y, k=0):
    return x + y + k


print(add_numbers(2, 3, k=8))

