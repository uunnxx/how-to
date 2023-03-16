import sys


for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
        # write the results to STDOUT
        # Reduce step
        # tab-delimeted; the word count is 1
        print(f"{word}\t1")
