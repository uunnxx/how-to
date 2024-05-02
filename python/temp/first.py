import time
import random
import threading


class Main():
    def __init__(self):
        print('clear')


def random_delay():
    return random.random() * 5

def random_countdown():
    return random.randrange(5)

def launch_rocket(delay, countdown):
    time.sleep(delay)
    for i in reversed(range(countdown)):
        print(f"{i + 1}...")
        time.sleep(1)
    print("Rocket launched")

def rockets():
    # N = 10_000
    N = 100
    return [
        (random_delay(), random_countdown())
        for _ in range(N)
    ]

def run_threads():
    threads = [
        threading.Thread(target=launch_rocket, args=(d, c))
        for d, c in rockets()
    ]
    for t in threads:
        t.start()

    for t in threads:
        t.join()



# if __name__ == '__main__':
#     for d, c in rockets():
#         launch_rocket(d, c)


if __name__ == '__main__':
    run_threads()


def my_func(asd):
    print(asd.capitalize())


my_func('text')
