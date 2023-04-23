import sys

args = list(sys.argv[1:])

if len(args) == 1 and ('coub.com' in args[0]):
    print(args[0])

print(args)

