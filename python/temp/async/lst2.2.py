async def coroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1


function_result = add_one(1)
coroutine_result = coroutine_add_one(1)

print(f"Result is equal to {function_result}, type is {type(function_result)}")
print(f"Result is equal to {coroutine_result}, type is {type(coroutine_result)}")
