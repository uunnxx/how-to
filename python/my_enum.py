def my_enum(sequence, start=0):
    count = start
    for item in sequence:
        yield count, item
        count += 1



a = ['a', 'b', 'c']

for i in my_enum(a):
    print(i)
