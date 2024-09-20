from threading import Thread, Lock
import time

lock = Lock()

def function_one():
    print("Thread one is aquiring the lock")
    lock.acquire()
    print("Thread one has acquired lock")
    time.sleep(2)
    lock.release()
    print("Thread one has released the lock")

def function_two():
    print("Thread two is aquiring the lock")
    lock.acquire()
    print("Thread two has acquired lock")
    time.sleep(2)
    lock.release()
    print("Thread two has released the lock")

thread1 = Thread(target=function_one)
thread2 = Thread(target=function_two)

thread1.start()
thread2.start()

thread1.join()
thread2.join()