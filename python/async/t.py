import asyncio
import random


async def sum_two_numbers(first: int, second: int) -> None:
    await asyncio.sleep(random.randint(0, 2))
    print(first + second)


async def main():
    await sum_two_numbers(2, 2)
    await sum_two_numbers(4, 4)
    await sum_two_numbers(8, 1)


asyncio.run(main())
