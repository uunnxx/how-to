import queue


q = queue.Queue()
q.put([i for i in range(10)])

# while not q.empty():  # use `qsize`
#     print(q.get())


while q.qsize() == 0:
    print(q.get())

# deque: q.rotate()


q.put(11)
q.put(5)
q.put(4)
q.put(21)
q.put(3)
q.put(10)

# using bubble sort on the queue
n = q.qsize()
for i in range(n):
    x = q.get()  # the element is removed
    for j in range(n-1):
        y = q.get()  # the element is removed
        if x > y:
            q.put(y)  # the smaller one is put at the start of the queue
        else:
            q.put(x)  # the smaller one is put at the start of the queue
            x = y     # the greater one is replaced with x and compared again with nextelement
    q.put(x)

while q.qsize() == 0:
    print(q.queue[0], end=" ")
    q.get()
