import _thread
import time

# _thread modul

def thread_fun(name, delay):

    for count in range(5):
        time.sleep(delay)
        print("%s: %s" %(name, time.ctime(time.time())))

def main():

    _thread.start_new_thread(thread_fun, ("thread_1", 2, ))
    _thread.start_new_thread(thread_fun, ("thread_2", 4, ))

if __name__ == "__main__":

    main()

    while 1:
        pass