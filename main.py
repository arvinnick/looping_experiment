"""
To find out the difference of looping vs vectorizing
"""
from time import time
import numpy as np


def looper(arr_):
    """
    Python vanilla looping for summation.
    :param arr_: sample numpy array for experiencing loop efficiency
    :return: sum of the arr_ elements
    """

    sum_ = 0
    for number in arr_:
        sum_ = sum_ + number
    return sum_

def vectorizer(arr_):
    """
    vectorized implementation for summation
    :param arr_: sample numpy array for experiencing loop efficiency
    :return: sum of the arr_ elements
    """
    return np.sum(arr_)

def main():
    """
    prints the timing results
    :return: None
    """
    timing = np.array([0,0])
    for i in range(200):
        print(i)
        arr = np.random.random(10000000)
        t_1_l = time()
        looper(arr)
        t_2_l = time()
        t_1_v = time()
        vectorizer(arr)
        t_2_v = time()
        timing = np.vstack([timing, [[1, t_2_l - t_1_l],
                                     [2, t_2_v - t_1_v]]])
    np.savetxt("timing.csv", timing)

if __name__ == "__main__":
    main()