import time


def heavy_work():
    for _ in range(100_000_000):
        pass


start_time = time.perf_counter()
heavy_work()
end_time = time.perf_counter()
print(f'Duration: {end_time - start_time}')



