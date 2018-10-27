from unittest import TestCase

# from searching.bin_search import search
# from searching.bin_search import iterative_search as search
from searching.bin_search import alg_bin_search as search

class TestSearch(TestCase):
    def test_in_list(self):
        self.assertEqual(search([1, 2, 3, 4], 4), 3)

    def test_out_list(self):
        self.assertEqual(search([1, 2, 3, 4], 5), -1)

    def test_in_list_odd1(self):
        self.assertEqual(search([1, 2, 3, 4, 9], 9), 4)

    def test_in_list_odd2(self):
        self.assertEqual(search([1, 2, 3, 4, 9], 3), 2)

    def test_out_list_odd(self):
        self.assertEqual(search([1, 2, 3, 4, 7], 5), -1)

    def test_empty(self):
        self.assertEqual(search([], 1), -1)

    def test_string(self):
        self.assertEqual(search(["a", "b", "d", "e"], "c"), -1)

    def test_string2(self):
        self.assertEqual(search(["a", "b", "d", "e"], "a"), 0)

    def test_none(self):
        self.assertEqual(search([1, 2, 3, 4, 6], None), -1)

    def test_multiple(self):
        self.assertEqual(search([1, 2, 2, 2, 2, 2, 3, 4, 6], 2), 1)

    def test_with_none(self):
        self.assertEqual(search([None, 1, 2, 3], None), 0)

    def test_with_none_1(self):
        self.assertEqual(search([None, 1, None, 3, 4], 1), 1)
