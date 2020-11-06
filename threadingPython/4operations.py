import threading 


def addition(number_1, number_2):

    print("numbers => %s, %s" %(number_1, number_2))
    print("result of addition => %d" %(int(number_1) + int(number_2)))
    return

def substraction(number_1, number_2):

    print("numvers => %s, %s" %(number_1, number_2))
    print("result of subtruction => %d" %(int(number_1 - int(number_2))))
    return 

def multiplication(number_1, number_2):

    print("numbers => %s, %s" %(number_1, number_2))
    print("result of multiplication => %d" %(int(number_1) * int(number_2)))
    return 

def division(number_1, number_2):

    print("numbers => %s, %s" %(number_1, number_2))
    
    try:
        result = number_1 / number_2
    except ZeroDivisionError as error:
        print("Error! ", error)
        result = 'None'
    print("result of division => %s" %(result))


def main():

    add_thread = threading.Thread(target=addition, args=(8,4))
    subs_thread = threading.Thread(target=substraction, args=(5,2))
    mult_thread = threading.Thread(target=multiplication, args=(4,7))
    div_thread = threading.Thread(target=division, args=(4,3))

    add_thread.start()
    subs_thread.start()
    mult_thread.start()
    div_thread.start()

if __name__ == "__main__":

    main()


