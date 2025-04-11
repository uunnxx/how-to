import threading


def hello_from_thread():
    print(f"Hello from the thread {threading.current_thread()}!")


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"At this time Python executing {total_threads} process(es)")
print(f"The name of the current thread {thread_name}")
hello_thread.join()
