import threading
import logging
import time
import concurrent.futures

 

class StoreIntoFile:

    def __init__(self):

        self.value = 0
    
    def update(self, threadName):

        logging.info("Thread %s: starting update", threadName) 
        _copy = self.value
        _copy += 1                                                          
        time.sleep(0.1)
        self.value = _copy

        with open("thread.txt", "w") as t_file:

            t_file.write(str(self.value))
            t_file.close()

        with open("thread.txt", "r") as tf:
            self.t = tf.read()

        logging.info("Thread %s: finishing update", threadName)


def main():

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level=logging.INFO, datefmt="%H:%M:%S") 
    SIF = StoreIntoFile()
    logging.info("Testing update. Starting value is %d.", SIF.value)

    for count in range(2):

        thread = threading.Thread(target=SIF.update, args=(count, ))
        thread.start()
    
    thread.join()
    logging.info("Testing update. Ending value is %s.", SIF.t)




if __name__ == "__main__":

    main()





