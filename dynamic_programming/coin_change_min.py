from unittest import TestCase

from dynamic_programming.coin_change import coin_change_min_top_down as solution

class TestCoinChange(TestCase):
    def test_1(self):
        self.assertEqual(solution(110, [1, 5, 10, 50]), 3)

    def test_2(self):
        self.assertEqual(solution(13, [1, 5, 6, 9]), 3)

    def test_3(self):
        self.assertEqual(solution(12, [1, 5, 6, 9]), 2)

    def test_not_found(self):
        self.assertEqual(solution(1, [2, 3, 4]), -1)
