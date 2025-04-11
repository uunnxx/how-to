import time
import requests

def read_example() -> None:
    response = requests.get('https://google.com')
    print(response.status_code)


sync_start = time.time()

read_example()
read_example()

sync_end = time.time()

print(f"Synchronous execution took {sync_end - sync_start:.4f} seconds.")
