import time
import random


# 'async' non blocking function
def timed_process(execution_time):
    start = time.time()
    while True:
        if time.time() - start < execution_time:
            yield
        else:
            yield
            break


# list of async funcs
processes = [timed_process(random.randint(1, 10)) for _ in range(100)]

# Execute funcs and remove from the waitlist
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
