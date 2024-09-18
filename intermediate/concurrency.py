# Threading & Time Modules
import threading
import time

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