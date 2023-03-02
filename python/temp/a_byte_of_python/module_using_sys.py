import sys

print('The command line arguments are: ')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is:\n', sys.path, '\n')
