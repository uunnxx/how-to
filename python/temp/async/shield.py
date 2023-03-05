import asyncio

from util import delay


async def main():
    task  = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except TimeoutError:
        print("The task took over 5 seconds, it'll finish soon!")
        result = await task
        print(result)


asyncio.run(main())
