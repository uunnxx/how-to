def manually_calling_close(filename):
    with open(filename, 'w') as f:
        f.write('hello\n')


# use `with` statement instead

def manually_calling_close2(filename):
    with open(filename) as f:
        f.write('hello\n')
