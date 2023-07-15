from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor as Executor


def async_map(executor, mapper, data):
    futures = []
    for datum in data:
        futures.append(executor.submit(mapper, datum))
    return futures


def map_less_naive(executor, my_input, mapper):
    return async_map(executor, mapper, my_input)


from time import sleep

def emitter(word):
    sleep(10)
    return word, 1


with Executor(max_workers=4) as executor:
    maps = map_less_naive(executor, words, emitter)
    print(maps[-1])


with Executor(max_workers=4) as executor:
    maps = map_less_naive(executor, words, emitter)
    not_done = 1
    while not_done > 0:
        not_done = 0
        for fut in maps:
            not_done += 1 if not fut.done() else 0
            sleep(1)
        print(f'Still not finalized: {not_done}')


def report_progress(futures, tag, callback):
    done = 0
    num_jobs = len(map_returns)
    while num_jobs > done:
        done = 0
        for fut in futures:
            if fut.done():
                done += 1
        sleep(.5)
        if callback:
            callback(tag, done, num_jobs - done)


def map_reduce_less_naive(my_input, mapper, reducer, callback=None):
    with Executor(max_workers=2) as executor:
        futures = async_map(executor, mapper, my_input)
        report_progress(futures, 'map', callback)
        map_results = map(lambda f: f.results(), futures)
        distributor = defaultdict(list)
        for key, value in map_results:
            distributor[key].append(value)

        futures = async_map(executor, reducer, distributor.items())
        report_progress(futures, 'reduce', callback)
        results = map(lambda f: f.results(), futures)
    return results
