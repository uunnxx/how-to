a = [1, 2, 3, 4, 5]


# for i in range(len(a)):
#     print(i)

D = 5


class Test():
    def tt(self, a, b):
        c = a + b
        return c


def test():
    for b in range(len(a)):
        print(b)
    # global D
    D = 88
    print(D)


test()

print(f"{D+2}")


ss = Test()

print(ss.tt(2, 2))
