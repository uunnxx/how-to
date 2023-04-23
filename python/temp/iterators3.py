class PowerTwo:
    # Class to implement an iterator of powers of two
    # Constructor accepting the max value
    def __init__(self, max=0):
        self.max = max

    # defined __iter__() to point the first element
    def __iter__(self):
        self.n = 1
        return self

    # __next__() to fetch the next value from the iterator
    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        result = 2 ** self.n
        self.n += 1
        return result


# create an object
numbers = PowerTwo(4)

# create an iterable from the object
i = iter(numbers)

# Using for-in loop to print the elements up to max
for it in i:
    print(it)
