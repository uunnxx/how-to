# Decorators
# Decorators are a shortcut to applying wrapper functions.
# This is helpful to 'wrap' functionality with the same code over and over
# again. For example, I cerated a 'retry' decorator for myself taht I can just
# apply to any function and if any exception is thrown during a run, it is
# retried again, till a maximum of 5 times and with a delay between each retry.
# This is especially useful for situations where you are trying to make
# a network call to a remote computer:

from time import sleep
from functools import wraps
import logging

logging.basicConfig()
log = logging.getLogger('retry')

def retry(f):
    @wraps(f)
    def warpper_function(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except Exception:
                log.exception('Attempt %s/%s failed : %s',
                              attempt,
                              MAX_ATTEMPTS,
                              (args, kwargs))
                sleep(10 * attempt)
        log.critical('All %s attempts failed : %s',
                     MAX_ATTEMPTS,
                     (args, kwargs))
    return warpper_function

counter = 0

@retry
def save_to_database(arg):
    print('Write to a database or make a network call or etc.')
    print('This will be automatically retried if exception is thrown.')
    global counter
    counter += 1
    # This will throw an exception in the first call
    # And will work fine in the second call (i.e. a retry)
    if counter < 2:
        raise ValueError(arg)

if __name__ == '__main__':
    save_to_database('Some bad value')
