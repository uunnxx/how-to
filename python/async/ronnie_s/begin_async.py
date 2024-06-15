import asyncio
from datetime import datetime

import click


async def sleep_and_print(seconds:  int) -> int:

    print(f'Starting {seconds} sleep')
    await asyncio.sleep(seconds)
    print(f'Finishing {seconds} sleep')

    return seconds



async def main():
    # results = await asyncio.gather(
    #     sleep_and_print(3),
    #     sleep_and_print(6)
    # )

    coroutine_list = []

    for i in range(1, 11):
        coroutine_list.append(sleep_and_print(i))

    results = await asyncio.gather(*coroutine_list)
    print(results)



start = datetime.now()
asyncio.run(main())
click.secho(f'{datetime.now() - start}', bold=True, bg='black', fg='yellow')
