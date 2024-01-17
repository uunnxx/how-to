import logging
import time


# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig()
log = logging.getLogger(__name__)


def expensive_function():
    time.sleep(2)
    return time.time()


if __name__ == '__main__':
    if log.isEnabledFor(logging.DEBUG):
        log.debug("The time  is %d", expensive_function())

