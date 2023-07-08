import array
v = memoryview(b'abcdefg')

print(v)

print(bytes(v[1:4]))


a = array.array('l', [-11111111, 22222222, -33333333, 444444444])

m = memoryview(a)

print(m[::2].tolist())
