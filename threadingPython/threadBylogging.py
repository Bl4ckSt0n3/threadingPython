import threading
import logging
import time

# create multiple thread and terminate all
def thread_function(threadName):

    logging.info("thread %s: starting", threadName)
    time.sleep(2)
    logging.info("thread %s: finishing", threadName)     

def main():

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level=logging.INFO, datefmt="%H:%M:%S")

    for count in range(2):                                                                    # multithreading into the loop
        thread = threading.Thread(target=thread_function, args=(count, ))
        thread.start()       

if __name__ == "__main__":

    main()
"""

import time
import threading
from threading import Thread


def ThreadFunction(i):
    print("Thread %i going to sleep for 5 seconds." % i)
    time.sleep(5)
    print("Thread %i is awake now." % i)


def Main():
  for i in range(10):
      myThread = Thread(target=ThreadFunction, args=(i, ))
      myThread.start()
      print("Current Thread count: %i." % threading.active_count())
    
    
if __name__ == "__main__":    
  Main()
"""



