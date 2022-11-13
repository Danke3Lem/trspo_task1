import random
import threading
import time

# Class 1 to create object №1
class Class_1:
    def __init__(self):
        self.__data = 0

    def write(self):
        return self.__data

    def read(self, data):
        self.__data = data

# Class 2 to create object №2
class Class_2:
    def __init__(self):
        self.__data = 0

    def write(self):
        return self.__data

    def read(self, data):
        self.__data = data

# Creating a function to create values in 1st part of all N-threads
def creatingThreadsPartOne(obj_1):
    K1 = random.randint(10000, 20000)

    for _ in range(K1):
        locker.acquire()

        try:
            obj_1_creating = random.randint(1, 70) + obj_1.write()
            obj_1.read(obj_1_creating)
        finally:
            locker.release()

# Creating a function to create values in 2nd part of all N-threads
def creatingThreadsPartTwo(obj_2):
    K2 = random.randint(10000, 20000)

    for _ in range(K2):
        locker.acquire()
        try:
            obj_2_creating = random.randint(1, 70) + obj_2.write()
            obj_2.read(obj_2_creating)
        finally:
            locker.release()


if __name__ == '__main__':
    t_start = time.time()

    obj_1 = Class_1()
    obj_2 = Class_2()

    # Calculating the whole amount of threads
    N = random.randint(10, 20)
    N1 = round(N/2)
    N2 = N-N1

    # Array to append all created threads to show them after all
    thr_list = []

    locker = threading.Lock()

    for i in range(N1):
        thr = threading.Thread(target=creatingThreadsPartOne, args=(obj_1,))
        thr_list.append(thr)

    for i in range(N2):
        thr = threading.Thread(target=creatingThreadsPartTwo, args=(obj_2,))
        thr_list.append(thr)

    for i in thr_list:
        i.start()

    for i in thr_list:
        i.join()

    t_end = time.time()
    total = "{:.3f}".format(t_end - t_start)
    print(f"Done! Total time: {total} sec.")
    print(f"Values we've got:\n\tobj_1: {obj_1.write()} |...| obj_2:{obj_2.write()}")