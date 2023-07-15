import asyncio
import pickle


results = {}

async def submit_job(reader, writer):
    job_id = max(list(results.keys()) + [0]) + 1
    writer.write(job_id.to_bytes(4, 'little'))
    results[job_id] = job_id * 3


async def get_results(reader, writer):
    job_id = int.from_bytes(await reader.read(4), 'little')
    pickle.dump(results.get(job_id, None), writer)


async def accept_requests(reader, writer):
    op = await reader.read(1)
    if op[0] == 0:
        await submit_job(reader, writer)
    elif op[0] == 1:
        await get_results(reader, writer)


async def main():
    server = await asyncio.start_server(accept_requests, '127.0.0.1', 1936)
    async with server:
        await server.serve_forever()

asyncio.run(main())
