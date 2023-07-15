import signal
import asyncio
from time import sleep as sync_sleep


def handle_interrupt_signal(server):
    server.close()
    while  server.is_serving():
        sync_sleep(0.1)


def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


async def main():
    server = await asyncio.start_server(accept_requests, '127.0.0.1', 1936)
    mp_pool = mp.Pool
