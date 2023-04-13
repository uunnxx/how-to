poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

with open('poem.txt') as f:
    while True:
        line = f.readline()
        # Zero length indicates EOF
        if len(line) == 0:
            break
        # The `line` already has a newline at the end of each line
        # since it is reading from a file.
        print(line, end='')
