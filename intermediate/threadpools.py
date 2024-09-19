# Concurrent Module - ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import time

def worker(number):
    print(f"Calculating result for {number}")
    time.sleep(2)
    return number ** 2

# Thread Pools
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