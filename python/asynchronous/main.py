import asyncio


async def perform_task():
    await asyncio.sleep(10)


async def main():
    tasks: list = []

    for task_id in range(1000):
        task = asyncio.create_task(perform_task())
        tasks.append(task)


    await asyncio.gather(*tasks)


