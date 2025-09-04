import threading, time

def background():
    while True:
        print("Background thread running")
        time.sleep(1)

t = threading.Thread(target=background, daemon=True)
t.start()

time.sleep(3)
print("Main program exiting")
time.sleep(3)