import asyncio


def blocking_function():
    pass

def non_blocking_function():
    pass


def sync_function(seconds: int):
    results = blocking_function()
    return results


async def async_function(seconds: int):
    results = await non_blocking_function()
    return results


# chaining

async def another_function():
    results = await async_function()
    return results




# 1. Async Python does not run itself.
# 2. We can only await from an async function.
# 3. Awaiting something does not magically make it async.


async def something():
    return 'ASYNC'


async def my_function(arg):
    await something()


# my_function(22)  # RuntimeWarning: coroutine 'my_function' was never awaited


async def my_function2(arg):
    res = await something()
    print(res)




asyncio.run(my_function2())
