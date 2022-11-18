from mpi4py import MPI
import random
import time
import sys
import numpy as np


# Function to calculate PI by throwing random points and counting each point that is in area
def calcPI(allPoints):
    amountOfPointsInside = 0

    for i in range(allPoints):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        dist = x ** 2 + y ** 2

        if dist <= 1:
            amountOfPointsInside += 1

    PI = 4.0 * amountOfPointsInside / allPoints
    return PI


def main():
    if (len(sys.argv) > 1):
        try:
            # Entering points as second argument throw the command line
            points = int(float((sys.argv[1])))
        except:
            print("ERROR! No arguments OR arguments shouldn't be int, but float.")

    else:
        print("Program is started, arguments are accepted.")
        exit()

    # initializing
    comm = MPI.COMM_WORLD
    mpiSize = comm.Get_size()
    mpiRank = comm.Get_rank()

    # Creating chunks and  distributing data evenly over them
    chunks = points % mpiSize
    myPoints = [points // mpiSize + 1] * chunks + [points // mpiSize] * (mpiSize - chunks)

    start = time.time()

    buffEnteringPI = np.ones(1) * calcPI(myPoints[mpiRank])

    end = time.time()
    resultTime = end - start

    for _ in range(0, mpiSize - 1):
        print("The core's # is - " + str(mpiRank) + ", time to calculate is - " + str(round(resultTime, 5))
              + " sec" + ", PI value is - " + str(buffEnteringPI))

    # Creating buff value to store calculated average PI
    buffStoringPI = np.zeros(1)

    # Reduces values on all processes to a single value by applying the operation SUM
    comm.Reduce(buffEnteringPI, buffStoringPI, op=MPI.SUM, root=0)

    # Creating average PI value
    buffStoringPI /= int(mpiSize)

    if mpiRank == 0:
        print("Amount of cores is - " + str(mpiSize) + ", average PI value is - " + str(round(buffStoringPI[0], 5)))


if __name__ == '__main__':
    main()