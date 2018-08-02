import unittest
from sorting.insertion_sort import insertion_sort as tested_sort


class SortTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual([], tested_sort([]))

    def test_one_zero(self):
        self.assertEqual([0], tested_sort([0]))

    def test_repeated_zeros(self):
        self.assertEqual([0, 0, 0], tested_sort([0, 0, 0]))

    def test_ascending(self):
        self.assertEqual([1, 2, 3, 4, 5], tested_sort([1, 2, 3, 4, 5]))

    def test_descending(self):
        self.assertEqual([1, 2, 3, 4, 5], tested_sort([5, 4, 3, 2, 1]))

    def test_permutation_one(self):
        self.assertEqual([0, 1], tested_sort([0, 1]))

    def test_permutation_two(self):
        self.assertEqual([0, 1], tested_sort([1, 0]))

    def test_out_of_order_one(self):
        test_list = [42, 9, 17, 54, 602, -3, 54, 999, -11]
        self.assertEqual(sorted(test_list), tested_sort(test_list))

    def test_out_of_order_two(self):
        test_list = [-11, -3, 9, 17, 42, 54, 54, 602, 999]
        self.assertEqual(sorted(test_list), tested_sort(test_list))

    def test_permutation_three(self):
        test_cases = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0], [0, 1, 1],
                      [1, 0, 1], [1, 1, 0]]
        for test_list in test_cases:
            self.assertEqual(sorted(test_list), tested_sort(test_list))
