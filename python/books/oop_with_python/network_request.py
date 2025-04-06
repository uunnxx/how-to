import time
import threading
from typing import Any, Callable


def network_request(number: int):
    time.sleep(1.0)
    return {'success': True, 'result': number ** 2}


def fetch_square(number: int):
    response = network_request(number)
    if response['success']:
        print(f"Result is: {response['result']}")


# fetch_square(2)

# Output:
# Result is: 4

# fetch_square(2)
# fetch_square(3)
# fetch_square(4)

# Output:
# Result is: 4
# Result is: 9
# Result is: 16


def wait_and_print(msg: str):
    time.sleep(1.0)
    print(msg)

def wait_and_print_async(msg: str):
    def callback():
        print(msg)

    timer = threading.Timer(1.0, callback)
    timer.start()


# Synchronous
# wait_and_print('First call')
# wait_and_print('Second call')
# print('After call')

# Output:
# <wait...>
# First call
# <wait...>
# Second call
# After call


# Asynchronous
wait_and_print_async('First async call')
wait_and_print_async('Second async call')
print('After submission')

# Output:
# After submission
# <wait...>
# First async call
# Second async call


def network_request_async(
        number: int,
        on_done: Callable[[dict[str, bool | int]], None]
) -> None:

    def timer_done():
        on_done({'success': True, 'result': number ** 2})

    timer = threading.Timer(1.0, timer_done)
    timer.start()


def on_done(result: dict[str, str]) -> None:
    print(result)

