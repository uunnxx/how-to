from thread_ import MyThread

threads = [
    MyThread('A', 0.5),
    MyThread('B', 0.7),
    MyThread('C', 0.5),
    MyThread('D', 1.0)
]


# threads = [thread1, thread2, thread3, thread4]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print('Finished')
