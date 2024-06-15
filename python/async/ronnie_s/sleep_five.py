import asyncio
from datetime import datetime

import click


async def sleep_five():
    pass


async def sleep_three_and_five():
    pass


async def main():
    results = ...
    print(results)


start = datetime.now()

asyncio.run(main())

click.secho(f'{datetime.now() - start}', bold=True, bg='black', fg='yellow')



