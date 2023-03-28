import time


class MyNumbers:
    # __iter__() is same as iter()
    def __iter__(self):
        self.a = 1
        return self

    # __next__() is same as next()
    def __next__(self):
        # 20th is the highest value
        if self.a <= 5:
            x = self.a
            # Manually increment
            self.a += 1
            # returning the iterator to the function call
            return x


# Create the object of the class
myclass = MyNumbers()
# get an iterator using iter()
myiter = iter(myclass)


for x in myiter:
    print(x)
    time.sleep(0.5)
