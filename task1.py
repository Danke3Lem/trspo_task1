import threading

def print_hello():
    print("Hello")

def print_koma():
    print(",")

def print_world():
    print("World")

def print_exclamation_mark():
    print("!")

if __name__ == "__main__":
    thread1=threading.Thread(target=print_hello())
    thread2=threading.Thread(target=print_koma())
    thread3=threading.Thread(target=print_world())
    thread4=threading.Thread(target=print_exclamation_mark())

    #starting all threads we have
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    #closing all threads we have
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    print("Threads are closed")
