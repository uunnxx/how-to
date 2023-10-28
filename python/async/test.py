import asyncio


async def bar(item: int) -> int:
    print("Started")
    await asyncio.sleep(1)
    print("Finished")
    return item ** 2

async def foo():
    items = range(1, 10)
    tasks = [bar(item) for item in items]
    new_items = await asyncio.gather(*tasks)
    return new_items

if __name__ == '__main__':
    results = asyncio.run(foo())
    print(results)

# Started
# ...
# Started
# Finished
# ...
# Finished
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
