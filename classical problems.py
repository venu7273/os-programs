
from time import sleep
from random import random
from threading import Thread
from queue import Queue


def producer(queue):
    print('Producer: Running')
    
    for i in range(10):
        
        value = random()
        
        sleep(value)
        
        item = (i, value)
        
        queue.put(item)
      
        print(f'>producer added {item}')
    
    queue.put(None)
    print('Producer: Done')


def consumer(queue):
    print('Consumer: Running')
    
    while True:
        
        item = queue.get()
       
        if item is None:
            break
        
        sleep(item[1])
       
        print(f'>consumer got {item}')
    
    print('Consumer: Done')


queue = Queue()

consumer = Thread(target=consumer, args=(queue,))
consumer.start()

producer = Thread(target=producer, args=(queue,))
producer.start()

producer.join()
consumer.join()
