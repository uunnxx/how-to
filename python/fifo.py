import queue


q = queue.LifoQueue()
q.put(list(range(10)))

while not q.empty():  # use `qsize`
    print(q.get())


while q.qsize() == 0:
    print(q.get())

# deque: q.rotate()
