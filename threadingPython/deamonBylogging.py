import threading
import logging
import time

def thread_fun(threadName):

    logging.info("thread %s: starting", threadName)
    time.sleep(2)
    logging.info("thread %s: finishing", threadName)



def main():

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level=logging.INFO, datefmt="%H:%M:%S")
    

    for index in range(2):

        logging.info("before starting thread %s", index)
        _thread = threading.Thread(target=thread_fun, args=(index, ), daemon=True)
        _thread.start()
        _thread.join()


    logging.info("done !")

if __name__ == "__main__":

    main()



