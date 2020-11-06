import threading
import time


# create a thread function 
def threadFun(threadNumber):

    print("thread {} is starting".format(threadNumber))
    time.sleep(2)
    print("thread {} is finishing".format(threadNumber))

def main():

    # loop to produce multithread 
    for i in range(4):
         # _thread value get threadFun as target value
        _thread = threading.Thread(target=threadFun, args=(i, ), daemon=True)     # we pass a parameter to Thread() that deamon 
        _thread.start() #   
        _thread.join() # join is used to joining 

if __name__ == "__main__":

    main()

