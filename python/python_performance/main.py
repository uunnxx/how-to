import time


def compute_inputs():
    time.sleep(1)
    return 123

INPUT = compute_inputs()

def something():
    time.sleep(1)
    return INPUT


def test_my_stuff(benchmark):
    result = benchmark(something)

    assert result == 123
