from collections.abc import Mapping
import time
import threading


class Main(threading.Thread):
    def __init__(self, map: Mapping[str, int]) -> None:
        super().__init__()
        self.map = map

    def run(self):
        for key, value in self.map.items():
            print(f'Sleeping for {value} sec.')
            print(key, value)
            time.sleep(value)


d = {'key1': 1, 'key2': 2, 'key3': 3}
m = Main(d)
m.start()

# d['key4'] = 4
