import threading
import time
import logging



def timerFun():
    logging.info("thread still running")
    return


def main():

    format = "(%(threadName)-5s): %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, )

    logging.info("before timerFun")
    time.sleep(1)
    timer_1 = threading.Timer(3.0, timerFun)
    timer_1.setName("Timer thread 1")
    
    timer_2 = threading.Timer(3.0, timerFun)
    timer_2.setName("Timer thread 2")
    
    logging.info("starting timer threads")
    timer_1.start()
    timer_2.start()

    logging.info("waiting for canceling %s ", timer_2.getName())
    time.sleep(2)
    logging.info("canceling %s", timer_2.getName())
    timer_2.cancel()
    time.sleep(2)
    print("Is alive Timer thread 2 ? : ", timer_2.is_alive())


    timer_1.join()
    timer_2.join()



if __name__ == "__main__":

    main()

