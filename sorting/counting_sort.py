import datetime
import random
import timeit
from matplotlib import pyplot as plt
import numpy as np


def find_domain(a_list):
    max_val = -float('inf')
    for item in a_list:
        if item > max_val:
            max_val = item
    return int(max_val)


def counting_sort(a_list):
    """Assume list of natural numbers only, including 0."""
    max_val = find_domain(a_list)
    buckets = [0] * (max_val+1)
    for item in a_list:
        buckets[item] += 1
    return [i for i, x in enumerate(buckets) for _ in range(x)]


def generate_test_cases(n, d):
    return [random.randint(0, d) for _ in range(n)]


if __name__ == '__main__':
    N = 1024
    M = [2**i for i in range(1000)]
    times = []
    random.seed(datetime.datetime.now())
    for domain_size in range(len(M)):
        start = timeit.default_timer()
        counting_sort(generate_test_cases(N, domain_size))
        end = timeit.default_timer() - start
        times.append(end)
    print([x for x in zip(M, times)])
    plt.scatter(M, times)
    plt.show()
