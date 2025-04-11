import time
import requests
import threading

def read_example() -> None:
    response = requests.get('https://google.com')
    print(response.status_code)


thread1 = threading.Thread(target=read_example)
thread2 = threading.Thread(target=read_example)

thread1.start()
thread2.start()

print('All threads are working!')

thread_start = time.time()

thread1.join()
thread2.join()

thread_end = time.time()

print(f"Synchronous execution took {thread_end - thread_start:.4f} seconds.")
