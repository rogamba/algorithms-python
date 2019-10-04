#lock_tut.py
from threading import Lock, Thread
lock = Lock()
g = 0

def add_one():
    print("Start add one")
    global g
    lock.acquire()
    g += 1
    lock.release()

def add_two():
    print("Start add two")
    global g
    lock.acquire()
    g += 2
    lock.release()

threads = []
for func in [add_one, add_two]:
    threads.append(Thread(target=func))
    threads[-1].start()

for thread in threads:
    """
    Waits for threads to complete before moving on with the main
    script.
    """
    thread.join()
    print("----")

print(g)