import sys


print(f"--> {sys.stdin.read()}\n")
print('this goes to stdout')
sys.stdout.write('this also goes to stdout')


sys.stdout.flush()  # sync

print('this goes to stderr', file=sys.stderr)
sys.stderr.write('this also goes to stderr')
