import os
from time import sleep
from threading import Thread

threads = [Thread(target=lambda: sleep(60)) for _ in range(10_000)]

[t.start() for t in threads]
print(f'PID = {os.getpid()}')
[t.join() for t in threads]
