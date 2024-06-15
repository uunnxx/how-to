import time
from datetime import datetime

import click


def sleep_and_print(seconds:  int) -> int:
    print(f'Starting {seconds} sleep')
    time.sleep(seconds)
    print(f'Finishing {seconds} sleep')


start = datetime.now()

print([sleep_and_print(3), sleep_and_print(6)])

click.secho(f'{datetime.now() - start}', bold=True, bg='black', fg='yellow')
