import sys
import time

f = None
try:
    with open('poem.txt') as f:
        # Our usual file-reading idiom
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            print(line, end='')
            sys.stdout.flush()
            print('Press ctrl+c now')
            # To make sure it runs for a while
            time.sleep(1)
except IOError:
    print('Could not find file poem.txt')
except KeyboardInterrupt:
    print('!! You cancelled the reading from the file.')
finally:
    if f:
        f.close()
    print('(Cleaning up: Closed the file)')

# The `with` statement
# with open('poem.txt') as f:
#     for line in f:
#         print(line, end='')
