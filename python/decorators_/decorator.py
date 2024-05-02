def decorate(func):
    def wrapper():
        print("wrapper")
        func()
    return wrapper


# def test():
#     print("test")
#


# => test = decorate(test)
@decorate
def testt():
    print('test')


test()
