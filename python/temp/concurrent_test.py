def br():
    print()
    print(f'{"-" * 34} break line {"-" * 34}')
    print()


tup = (1, True, 'red')

br()
print(tup)


from collections import namedtuple

A = namedtuple('A', 'count enabled color')

tup = A(count=1, enabled=True, color='red')

print(tup.count)
print(tup.enabled)
print(tup.color)
print(tup)

print(A)


br()



def f():
    return 2, False, 'blue'

count, enabled, color = f()

print(count, enabled, color)


tup= f()
enabled = tup[1]

print(enabled)
print(tup)




from time import perf_counter
from array import array
from contextlib import contextmanager

@contextmanager
def timing(label: str):
    t0 = perf_counter()
    yield lambda: (label, t1 - t0)
    t1 = perf_counter()

with timing('Array tests') as total:
    with timing('Array creation innermul') as inner:
        x = array('d', [0] * 1_000_000)

    with timing('Array creation outermul') as outer:
        x = array('d', [0]) * 1_000_000

print('Total  [%s]: %.6f s' % total())
print('Timing [%s]: %.6f s ' %inner())
print('Timing [%s]: %.6f s ' %outer())

br()

import threading

def work():
    return sum(x for x in range(1_000_000))

thread = threading.Thread(target = work)
print(thread)
thread.start()
thread.join()
print(thread)


br()


from concurrent.futures import ThreadPoolExecutor as Executor

urls = '''
google twitter facebook youtube pointerst tumblr instagram reddit flickr meetup classmates microsoft apple linkedin xing renren disqus snapchat twoo whatsapp
'''.split()

def fetch(url):
    from urllib import request, error
    try:
        data = request.urlopen(url).read()
        return '{}: length {}'.format(url, len(data))
    except error.HTTPError as e:
        return '{}: {}'.format(url, e)

with Executor(max_workers=4) as exe:
    template = 'http://www.{}.com'
    jobs = [exe.submit(fetch, template.format(u)) for u in urls]
    results = [job.result() for job in jobs]

# print('\n'.join(results))





br()
















br()
