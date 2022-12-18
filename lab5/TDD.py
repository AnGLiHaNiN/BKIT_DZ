import unittest.mock
from lab5 import get_roots, sort_with_lambda, gen_random
import sys

def compare_list(lst1, lst2):
    return len(lst1) == len(lst2) and set(lst1) == set(lst2)

class TestFuncs(unittest.TestCase):
    def test_calculate(self):
        tests = [
            ([1, 1, -2], [1, -1]),
            ([9, 8, -1], [0.3333333333333333, -0.3333333333333333]),
            ([20, -1, -1], [0.5, -0.5]),
            ([1, -40, 144], [6, -6, 2, -2]),
            ([5, -4, 1], []),
            ([-4, 16, 0], [2, -2, 0]),
            ([1, -18, 81], [3, -3]),
            ([256, -32, 1], [0.25, -0.25]),
            ([4, 0, 0], [0]),
            ([1, 0.1, 0], [0]),
        ]
        for test in tests:
            roots = get_roots(*test[0])
            self.assertTrue(compare_list(roots, test[1]))

    def test_sort_with_lambda(self):
        tests = [
            ([3, -40, 40, 4, 5], [-40, 40, 5, 4, 3]),
            ([1, 5, 3, -4, 2], [5, -4, 3, 2, 1]),
        ]
        for test in tests:
            sequence = sort_with_lambda(test[0])
            self.assertListEqual(sequence, test[1])

        #sequence = [1,5,3,-4,2]
        #self.assertListEqual(sort_with_lambda(sequence), [5,-4, 3, 2, 1])

    def test_gen_random(self):
        sequence = list(gen_random(5,1,3))
        self.assertEqual(len(sequence),5)

if __name__ == "__main__":
    unittest.main()