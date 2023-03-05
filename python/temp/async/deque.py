from collections import deque


messages = deque()

while True:
    if messages:
        message = messages.pop()
        process_message(message)


def make_request():
    cpu_bound_setup()
    io_bound_web_request()
    cpu_bound_postprocess()

task_one = make_request()
task_two = make_request()
task_three = make_request()


