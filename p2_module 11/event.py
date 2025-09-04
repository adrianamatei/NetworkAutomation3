import threading, time

event = threading.Event()

def waiter():
     print("Waiting for event to be set...")
     event.wait()
     print("Event detected, continuing")

def setter():
     time.sleep(2)
     print("Setting event")
     event.set()

threading.Thread(target=waiter).start()
threading.Thread(target=setter).start()