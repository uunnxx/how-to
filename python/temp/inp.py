while True:
    inp = input()
    print(inp)

    if inp == '':
        print('Empty string')
    elif inp == 'stop':
        break
    elif inp == '\n':
        print('New line')

