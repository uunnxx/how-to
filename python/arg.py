import sys

print(sys.argv)
def argument_parse():
    given = sys.argv[1:]
    match given:
        case [coub] if 'coub.com' in coub:
            print('coub link')
            print(coub)
        case ['pause']:
            print('paused')
        case ['play']:
            print('played')
        case ['next']:
            print('next file')
        case ['prev']:
            print('previous file')


argument_parse()
