def manually_calling_close(filename):
    f = open(filename, 'w')
    f.write('hello\n')
    f.close()


# use `with` statement instead

def manually_calling_close2(filename):
    with open(filename) as f:
        f.write('hello\n')
