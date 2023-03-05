import asyncio

from asyncio import CancelledError
from util import delay


async def main():
    long_task = asyncio.create_task(delay(10))

    second_elapsed = 0

    while not long_task.done():
        print('not over yet')
        await asyncio.sleep(1)
        second_elapsed += 1
        if second_elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print('The task were cancelled!')


asyncio.run(main())
