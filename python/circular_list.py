class CircularList:
    def __init__(self, *args):
        self.n = len(args)
        self.lst = args
        self.i = None

    def next(self):
        if self.i is None:
            self.i = -1
        self.i = (self.i + 1) % self.n
        return self.lst[self.i]

    def prev(self):
        if self.i is None:
            self.i = 0
        self.i = (self.i - 1) % self.n
        return self.lst[self.i]
