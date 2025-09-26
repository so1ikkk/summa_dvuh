import unittest
from main import twosum

class TestMath(unittest.TestCase):

    def test_two_sum(self):
        self.assertEqual(twosum([2, 7, 11, 15], 9), [0, 1])
    def test_two_sum_2(self):
        self.assertEqual(twosum([3,2,4], 6), [1, 2])
    def test_two_sum_3(self):
        self.assertEqual(twosum([3,3],6), [0,1])
    def test_nosolution(self):
        self.assertEqual(twosum([1, 2, 3], 7), None)
    def test_negatives(self):
        self.assertEqual(twosum([-3, 4, 3, 90], 0), [0, 2])
    def test_zeros(self):
        self.assertEqual(twosum([0, 4, 3, 0], 3), [0, 2])
    def test_empty(self):
        self.assertEqual(twosum([], 5), None)


if __name__ == '__main__':
    unittest.main()