import concurrent.futures
import logging
import time
 

def thread_function(threadName):

    logging.info("thread %s: starting", threadName) 
    time.sleep(2)
    logging.info("thread %s: finishing", threadName)

def main():

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level=logging.INFO, datefmt="%H:%M:%S")

    # threading by ThreadPoolExecuter
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(thread_function, range(5))

if __name__ == "__main__":                      

    main()