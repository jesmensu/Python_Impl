import time
from random import randint
import threading

queue = []

def produce():
    for i in range(0,5):
        time.sleep(1)
        queue.append(i*i)

def consume():
    while True:
        if len(queue) > 0:
            val = queue.pop()
            print(val)

if "__name__"=="__main__":
    p = threading.Thread(target=produce)
    c = threading.Thread(target=consume)

    p.start()
    c.start()
