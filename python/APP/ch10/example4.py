import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print(f'Starting thread {self.name}')
        thread_lock.acquire()
        thread_count_down(self.name, self.delay)
        thread_lock.release()
        print(f'Finished thread {self.name}')


def thread_count_down(name, delay):
    counter = 5

    while counter:
        time.sleep(delay)
        print(f'Thread {name} counting down: {counter}...')
        counter -= 1

thread_lock = threading.Lock()

thread1 = MyThread('A', 0.5)
thread2 = MyThread('B', 0.5)

thread1.start()
thread2.start()


thread1.join()
thread2.join()


# threads = [MyThread('A', 0.5), MyThread('B', 0.5)]
#
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
