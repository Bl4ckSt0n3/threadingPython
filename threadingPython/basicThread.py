import threading
import time


def createThread(threadNumber):

    print("thread {} created".format(threadNumber))
    time.sleep(1)
    print("thread {} has done".format(threadNumber))

def  main():

    print("before creating thread !")

    for _tNum in range(4):

        _thread = threading.Thread(target=createThread, args=(_tNum, ))
        _thread.start()

if __name__ == "__main__":

    main()