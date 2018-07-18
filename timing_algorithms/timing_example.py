import random
import timeit
from datetime import datetime

import numpy as np
import pandas as pd


def generate_testcase(n):
    random.randrange(0, 1)
    random.seed(datetime.now())
    return [random.random() for _ in range(n)]


def timer(func):
    def wrapped_func(*args, **kwargs):
        start = timeit.default_timer()
        func(*args, **kwargs)
        end = timeit.default_timer()
        # print("elapsed for {.__name__}".format(func), end - start)
        return end - start
    return wrapped_func     # returns the wrapped function as an object


@timer      # decorator - python shorthand for insertion_sort = timer(insertion_sort)
def insertion_sort(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i + 1] < a_list[i]:
            a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
            for j in range(i, 0, -1):
                if a_list[j] < a_list[j - 1]:
                    a_list[j], a_list[j - 1] = a_list[j - 1], a_list[j]
                else:
                    break
    return a_list


@timer
def selection_sort(a_list):
    for i in range(len(a_list)):
        min_index = 0
        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_index]:
                min_index = j
        a_list[min_index], a_list[i] = a_list[i], a_list[min_index]
    return a_list


@timer
def bubble_sort(a_list):
    for i in range(len(a_list) - 1):
        swapped = False
        for j in range(len(a_list) - 1):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                swapped = True
        if not swapped:
            break
    return a_list


@timer
def shaker_sort(a_list):
    swapped = False
    lo = 0
    hi = len(a_list) - 1
    while not swapped:
        for j in range(lo, hi):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                swapped = True
        if not swapped:
            break
        hi -= 1
        swapped = False
        for j in range(hi, lo, -1):
            if a_list[j] < a_list[j - 1]:
                a_list[j], a_list[j - 1] = a_list[j - 1], a_list[j]
                swapped = True
        lo += 1
        if not swapped:
            break
        else:
            swapped = False
    return a_list


def main():
    n_values = [2 ** i for i in range(1, 11)]
    sorting_alg = ["insertion_sort", "selection_sort", "bubble_sort", "shaker_sort"]
    functions_to_test = [insertion_sort, selection_sort, bubble_sort, shaker_sort]
    results = np.zeros([len(n_values), len(functions_to_test)])
    for i, func in enumerate(functions_to_test):
        for j, n in enumerate(n_values):
            results[j][i] = func(generate_testcase(n))
    df = pd.DataFrame(results, n_values, sorting_alg)
    print(df)


if __name__ == '__main__':
    main()
