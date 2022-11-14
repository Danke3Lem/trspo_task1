import threading
import time
from queue import Queue

# Creating a queue to store all elements that we are going to evolute
queue = Queue()
# Saving our results for each value
results_arr = []
# Creating a lock to control threads' access to the values and functions
lock = threading.Lock()

# Creating a class to store an info about each element(number, its evolved value, the count of step where we are)
class CollatzConjectureNumber:
    def __init__(self, num):
        self.num = num
        self.changed_num = num
        self.stepsCount = 0

# Function to calculate the evolution for each value and catch a breakpoint
def collatzConjecture():
    while True:
        if len(results_arr) != N:
            value = queue.get()
            if value.changed_num == 1:
                lock.acquire()
                results_arr.append(value)
                lock.release()
            else:
                 if value.changed_num % 2 != 0:
                    value.changed_num = 3 * value.changed_num + 1
                 else:
                    value.changed_num /= 2
                 value.stepsCount += 1
                 queue.put(value)
        else:
            break


if __name__ == '__main__':
    N = int(input("Enter a number to create a list of numbers from 1 to N: "))
    thr_amount = int(input("Enter a number to create N threads: "))

    # Creating a list of numbers we'll use
    for i in range(1, N + 1):
        queue.put(item=CollatzConjectureNumber(i))

    t_start = time.time()

    # Creating a list of threads that we'll use to calculate the task
    thr_list = []
    for i in range(thr_amount + 1):
        thr_list.append(threading.Thread(target=collatzConjecture, args=()))

    for i in thr_list:
        i.start()

    for i in thr_list:
        i.join()

    t_end = time.time()
    total = "{:.3f}".format(t_end - t_start)
    print(f"Done! Total time: {total} sec.")