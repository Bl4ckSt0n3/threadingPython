import threading
import logging
import time

# solving race condition with lock

class StoreIntoFile:

    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def locked_update(self, threadName):       # function starts for both threads
        logging.info("Thread %s: starting update", threadName)    # thread 0 is starting and after thread 1
        logging.debug("Thread %s about to lock", threadName)      # 

        with self._lock:

            logging.debug("Thread %s has lock", threadName)
            _copy = self._value
            _copy += 1                                                          
            time.sleep(0.1)
            self._value = _copy
            logging.debug("Thread %s about to open the lock", threadName)     #

            with open("threadFile.txt", "w") as FILE:
                FILE.write(str(self._value))

            with open("threadFile.txt", "r") as F:
                self._readFile = F.read()
                     
        logging.debug("Thread %s after open the lock", threadName)
        logging.info("Thread %s: finishing update", threadName)


if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level=logging.INFO, datefmt="%H:%M:%S") 
    SIF = StoreIntoFile()
    logging.info("Testing update. Starting value is %d.", SIF._value)
 
    for count in range(4):
        thread = threading.Thread(target=SIF.locked_update, args=(count, ))
        thread.start()
    

    logging.getLogger().setLevel(logging.DEBUG) # used for activate debug level
    thread.join()
    logging.info("Testing update. Ending value is %s.", SIF._value)
    #logging.info("Testing update. Ending value is %s.", SIF._readFile)
    