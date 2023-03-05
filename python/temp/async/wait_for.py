import asyncio

from util import delay


async def main():
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Timeout! 1 second was passed!')
        print(f"Is the task were cancelled? {delay_task.cancelled()}")


asyncio.run(main())
