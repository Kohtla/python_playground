import time
import random


def timed_process(execution_time):
    start = time.time()
    while True:
        if time.time() - start < execution_time:
            yield
        else:
            yield
            break


processes = [timed_process(random.randint(1, 10)) for _ in range(100)]

start = time.time()
while True:
    print(f"Processes count: {len(processes)}")
    for process in processes:
        try:
            process.send(None)
        except StopIteration:
            processes.remove(process)
    if len(processes) == 0:
        print(f"Job is done at {time.time() - start}")
        break
