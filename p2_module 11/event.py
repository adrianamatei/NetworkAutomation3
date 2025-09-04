import threading
import time
event = threading.Event()
def waiter():
    print("waiting for event to be set ")
    event.wait()
    print("event detected, continuing")
def setter():
    time.sleep(2)
    print("setting event")
    event.set()
threading.Thread(target=waiter).start()
threading.Thread(target=setter).start()