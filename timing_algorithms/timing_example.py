import random
import timeit
from datetime import datetime
from Algorithms.sorting import *

import numpy as np
import pandas as pd


def generate_testcase(n):
    random.randrange(0, 1)
    random.seed(datetime.now())
    return [random.random() for _ in range(n)]


# use @timer over an algorithm to measure its runtime; equivalent to func = timer(func)
def timer(func):
    def wrapped_func(*args, **kwargs):
        start = timeit.default_timer()
        func(*args, **kwargs)
        end = timeit.default_timer()
        # print("elapsed for {.__name__}".format(func), end - start)
        return end - start
    return wrapped_func     # returns the wrapped function as an object


def main():
    n_values = [2 ** i for i in range(1, 11)]
    sorting_alg = ["insertion_sort", "selection_sort", "bubble_sort", "shaker_sort"]
    functions_to_test = [insertion_sort.insertion_sort,
                         selection_sort.selection_sort,
                         bubble_sort.bubble_sort,
                         shaker_sort.cocktail_shaker]
    results = np.zeros([len(n_values), len(functions_to_test)])
    for i, func in enumerate(functions_to_test):
        for j, n in enumerate(n_values):
            results[j][i] = (timer(func)(generate_testcase(n)))
    df = pd.DataFrame(results, n_values, sorting_alg)
    print(df)


if __name__ == '__main__':
    main()
