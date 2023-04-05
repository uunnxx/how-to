import asyncio
from contextlib import contextmanager, suppress
from typing import Any, List


async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    try:
        f.set_result('I have finished.!')
    except RuntimeError as e:
        print(f"No longer allowed: {e}")
        f.cancel()


loop = asyncio.get_event_loop()
fut = asyncio.Task(asyncio.sleep(1_000_000))
print(fut.done())


loop.create_task(main(fut))
with suppress(asyncio.CancelledError):
    loop.run_until_complete(fut)


print(fut.done())
print(fut.cancelled())




async def f():
    pass


coro = f()
loop = asyncio.get_event_loop()

task = loop.create_task(coro)
assert isinstance(task, asyncio.Task)

new_task = asyncio.ensure_future(coro)
assert isinstance(new_task, asyncio.Task)

mystery_meat = asyncio.ensure_future(task)
assert mystery_meat is task


def listify(x: Any) -> List:
    '''Try hard to convert x into a list'''
    if isinstance(x, (str, bytes)):
        return [x]

    try:
        return [_ for _ in x]
    except TypeError:
        return [x]


class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return conn

    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()


async with Connection('localhost', 9001) as conn:
    # ...




@contextmanager
def web_page(url):
    data = download_webpage(url)
    yield data
    update_stats(url)


with web_page('google.com') as data:
    process(data)


class A:
    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x > 2:
            raise StopIteration
        else:
            self.x += 1
            return self.x


for i in A():
    print(i)

##########################


class B():
    def __init__(self):
        return self

