import unittest, copy
from abstract_data_types.priority_queue import *

class PriorityQueueTest(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()
        self.fullPq = PriorityQueue()
        self.tests = [(1, "a"), (10, "b"), (100, "c"), (1000, "d"), (10000, "e")]
        self.testRes = sorted([(-1, "a"), (-10, "b"), (-100, "c"), (-1000, "d"), (-10000, "e")], key= lambda x: x[0])
        for test in self.tests:
            self.fullPq.add(test[0], test[1])

    def test_push_one(self):
        test = self.tests[0]
        self.pq.add(test[0], test[1])
        self.assertEqual((-1 * test[0], test[1]), self.pq.array[0])

    def test_push_two(self):
        a = []
        while len(self.fullPq) != 0:
            a.append(self.fullPq.pop())
        self.assertEqual(self.testRes, a)

    def test_peek_one(self):
        self.assertEqual(self.testRes[0], self.fullPq.peek())

    def test_peek_two(self):
        before_peek = copy.deepcopy(self.fullPq)
        self.fullPq.peek()
        self.assertEqual(str(before_peek), str(self.fullPq))

    def test_empty_queue(self):
        with self.assertRaises(EmptyQueueError):
            self.pq.pop()