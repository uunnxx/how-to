import asyncio


# async def some_func():
#     print('Done sleepnig')
#     await asyncio.sleep(1)
#     print('Done sleepnig')
#
#
# asyncio.run(some_func())


# async def speak():
#     print('Hey!')
#
#
# async def run():
#     await speak()
#
#
# asyncio.run(run())


async def my_async_func():
    print('B')
    await asyncio.sleep(1)
    print('C')


async def run():
    async_func = my_async_func()
    print('A')
    await async_func


asyncio.run(run())
