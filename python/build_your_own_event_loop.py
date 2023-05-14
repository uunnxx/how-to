# A While loop
# At its core, the Event Loop is a while loop that iterates through the tasks and executes them.


# while tasks:
#     for task in tasks:
#         execute(task)



# Task Queue
# The task queue contains the tasks that need to be executed. The Event Loop constantly iterates through these tasks and executes them. Tasks can be repeatedly added to the queue when they need to be executed.

from collections import deque

tasks = deque()

def task_1(): print('Task 1')
def task_2(): print('Task 2')

tasks.append(task_1)
tasks.append(task_2)


while tasks:
    task = tasks.popleft()
    task()

# Tasks
# To execute tasks concurrently we need to add them to the tasks queue in
# an alternating fashion. Take the following snippet for example.
# We cannot isolate each iteration of the for loop and execute it independently.
# The for loop is a sequential construct.

# Can't execute concurrently:
def countup(n):
    for i in range(n):
        print(f'Printing {i}')

def countdown(n):
    for i in range(n):
        print(f'Printing {n - i}')

tasks.add(lambda: countup(5))
tasks.add(lambda: countdown(5))

# However, if we alter the code to use recursive calls, we can add them to the
# task queue, and achieve a level of concurrency.

# Can execute concurrently:
def countup(n):
    print(f'Printing {i}')
    tasks.add(lambda: countup(n - 1))

def countdown(n):
    def _run(i):
        print(f'Printing {i}')
        tasks.add(lambda: _run(n - 1))
    _run(n - 1)

tasks.add(lambda: countup(5))
tasks.add(lambda: countdown(5))

# A non-blocking sleep call
# The `time.sleep()` call in Python is a blocking call. Calling the
# `time.sleep()` within a program pauses the execution of the entire program
# within Python and blocks other tasks from executing. This outcome might
# wish to delay only certain functions and not the entire program.
# Asyncio mitigates this problem by suspending the current function and
# switching to the next one in task queue.


import time
from collections import deque

sleeping = []
ready = deque()

# Add func to sleeping queue with deadline
def schedule_task(task, delay):
    deadline = time.time() + delay
    sleeping.append((deadline, task))

schedule_task(lambda: print('Printing after delay'), 5) # 5 second delay


# The `schedule_task` function above calculates the deadline for the task
# to be executed and adds to along with the function to the sleeping queue.
# On every iteration, the Event Loop checks if the deadline has expired.
# If it has, the task is moved to the ready queue.

while ready or sleeping:
    if not ready:
        deadline, task = sleeping.pop()
        delta = deadline - time.time()
        if delta < 0:  # check if deadline is over
            ready.append(task)
        # execute task
        while ready:
            task = ready.popleft()
            task()


# Non-Blocking sockets for Network I/O
# The traditional `send` and `recv` socket calls are blocking in nature.
# If there is no message to be received, the `recv` system calls will block
# the program until it recieves a message. To get around this issue we can use
# the `select` call. The `select` call will provide us with the status of the
# socket i.e. if there is a message waiting to be read, or if a message has
# been sent. Using the selectcall, we can call `recv` only when there is a
# messages only when the write buffer is free.

readable, writable, _ = select([socket], [socket], [], timeout = 0.2)
for read_sock in readable:
    read_sock.recv(1000)  # Read from socket

for write_sock in writable:
    write_sock.send('hello')  # Write to socket

# Let's build a non-blocking socket-based server that echoes the input
# back to the client. Initialize your socket as follows.

import socket
from select import select
from collections import deque

readable_t = {}
writable_t = {}
tasks = deque()

addr = ('127.0.0.1', 3000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(1)
sock.setblocking(False)

# The `readable_t` and `writable_t` dictionaries above hold the callbacks
# for the read and write events for a socket.

# Let's also have 3 non-blocking function calls that add the task to the task
# queue. These functions are primarely meant to accept, send and recieve
# messages.

def accept(sock):
    '''
    Callback to accept connections from a client
    '''
    client, addr = sock.accept()
    # adds recv to read map
    readable_t[client]] = lambda: recv(client)

def recv(client):
    '''
    Callback to recieve message from a client
    '''
    data = client.recv(10000)
    # adds send to write map
    writable_t[client] = lambda: send(client, data)

def send(sock, data):
    '''
    Callback to send message to the client.
    '''
    sock.send(b'Got: ' + data)
    # adds recv to read map once the message is sent
    readable_t[sock] = lambda: recv(sock)

# Note that these functions do not actually send or recieve messages.
# They just facilitate it by adding the tasks to the task queue.

# The following snippet watches for any messages and if found, calls the
# accept function. The while loop iteratively checks for any messages
# that have arrived or departed and adds the respective read/write calls
# to the task queue.

readable_t[sock] = lambda: accept(sock)

while True:
    # check is anything has to be read or written
    readable, writable, _ = \
        select(readable_t.keys(), writable_t.keys(), [], 0.2)
