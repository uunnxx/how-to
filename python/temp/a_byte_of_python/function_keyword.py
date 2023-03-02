def func(a, b = 5, c = 10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3)
func(3, 7)
func(3, c = 24)
func(c = 24, a = 100)
