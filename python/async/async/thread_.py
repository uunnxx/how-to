import os
import threading

print(f"Running Python-process s id: {os.getpid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"At this time Python executing {total_threads} process(es)")
print(f"The name of the current thread {thread_name}")
