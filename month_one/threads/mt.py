# Concurrency (Concept) : How a program or algorithm is structured, not how it is executed
#                         Several sub parts can be executed out of order without affecting outcome (no specific order, identical final result)

# Threading & Time Modules
import threading
import time
import random

# Concurrent Module - ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor

# Target Functions
def call_api(path):
    time.sleep(5)
    print(f"{path} was called.")

def parse_json():
    time.sleep(10)
    print("JSON response was parsed.")

def persist_data(data):
    time.sleep(5)
    print(f"{data} was persisted.")

# Single-Threaded Method Call
# call_api()
# take_out_trash()
# persist_data()

# Creating & Starting Threads
thread1 = threading.Thread(target=call_api, args=("http://testapi/api/v1/players/TOR",))
thread1.start()

thread2 = threading.Thread(target=parse_json)
thread2.start()

thread3 = threading.Thread(target=persist_data, args=("{\"first_name\": \"Auston\", \"last_name\": \"Matthews\"}",))
thread3.start()

# Join Method Call To Wait On Threads Before Program Termination
thread1.join()
thread2.join()
thread3.join()
print("All threads are complete.")

# Thread Pools
def worker(number):
    print(f"Calculating result for {number}")
    time.sleep(2)
    return number ** 2

pool = ThreadPoolExecutor(5)
result1 = pool.submit(worker, 7)
result2 = pool.submit(worker, 9)
result3 = pool.submit(worker, 5)
result4 = pool.submit(worker, 5)
result5 = pool.submit(worker, 8)

# time.sleep(5)
if result3.done():
    print(result3.result())

# pool.shutdown() Prevents any further submissions

print("End of file")

# Locks & Synchronization
# lock = threading.Lock()
# lock.acquire(blocking=True, timeout=3)
# r_lock = threading.RLock()
# with lock:


class ThreadCounter:

    def __init__(self):
        self.counter = 0
        self.lock = threading.Lock()

    def count(self, thread_no):
        while True:
            self.lock.acquire()
            self.counter += 1
            print(f"{thread_no}: Just increased counter to {self.counter}")
            time.sleep(1)
            print(f"{thread_no}: Done some work, now value is {self.counter}")
            self.lock.release()
            time.sleep(random.randint(1,3))

tc = ThreadCounter()

for i in range(30):
    t = threading.Thread(target=tc.count, args=(i,))
    t.start()