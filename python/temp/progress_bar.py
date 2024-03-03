# simple progress bar


import sys
import time


def progress_bar(count, total=100, suffix=''):
    bar_length = 100
    filled_length = int(round(bar_length * count / float(total)))

    percent = round(100.0 * count / float(total), 1)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write(f'[{bar}] {percent}% ...{suffix}\r')
    sys.stdout.flush()


for i in range(100):
    time.sleep(0.1)
    progress_bar(i)
