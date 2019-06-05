import unittest
import lesson22_sort_fast as l
import random
from lesson21_bubble_selection import sort_shell


class FastSortTest(unittest.TestCase):

    def test_sort_fast(self):
        n1 = [8, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 8, 8]
        n2 = [12, 16, 6, 1, 20, 11, 4, 10, 3, 13, 9, 1, 2, 5, 10, 12, 1, 18, 3, 11]
        result1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 9, 10, 11, 12, 13, 14, 15]
        result2 = [1, 1, 1, 2, 3, 3, 4, 5, 6, 9, 10, 10, 11, 11, 12, 12, 13, 16, 18, 20]
        l.sort_fast(n1, 0, len(n1) - 1)
        l.sort_fast(n2, 0, len(n2) - 1)
        self.assertListEqual(n1, result1)
        self.assertListEqual(n2, result2)

    def test_sort_shell(self):
        test = [random.randint(0, pow(10, 5)) for i in range(5 * pow(10, 5))]
        sort_shell(test)

    def test_sort_fast2(self):
        test = [random.randint(0, pow(10, 5)) for i in range(5 * pow(10, 5))]
        l.sort_fast(test, 0, len(test)-1)



if __name__ == '__main__':
    unittest.main()
