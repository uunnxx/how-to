import asyncio


class Asynchronous_Iterator:
    ''' Iterate over an asynchronous source. n Iterations.'''

    def __init__(self, n):
        self.current = 0
        self.n = n

    def __aiter__(self):
        return self

    async def __anext__(self):
        await asyncio.sleep(1)
        print(f"get next element {self.current}")
        self.current += 1
        if self.current > self.n:
            raise StopAsyncIteration
        return self.current - 1


async def main():
    async for i in Asynchronous_Iterator(3):
        print(f"next element {i}")


asyncio.run(main())
