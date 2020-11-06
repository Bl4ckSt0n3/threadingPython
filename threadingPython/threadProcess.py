import threading
import logging
import time
import _thread
import concurrent.futures



# create multiple thread and terminate them
def thread_function(threadName):

    logging.info("thread %s: starting", threadName)
    time.sleep(2)
    logging.info("thread %s: finishing", threadName)

if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level=logging.INFO, datefmt="%H:%M:%S")
    list_of_threads = []

    for count in range(2):

        logging.info("Main    : create and start thread %d.", count)
        thread = threading.Thread(target=thread_function, args=(count, ))
        list_of_threads.append(thread)
        thread.start()
    
    # list all threads
    for index, thrd in enumerate(list_of_threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
    














