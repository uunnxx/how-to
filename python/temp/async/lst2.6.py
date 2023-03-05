import asyncio


async def delay(delay_seconds: int) -> int:
    print(f"Sleeping for {delay_seconds} sec")
    await asyncio.sleep(delay_seconds)
    print(f"{delay_seconds} second is over")
    return delay_seconds
