import unittest
import lesson22_sort_fast as l


class FastSortTest(unittest.TestCase):

    def test_sort_insert(self):
        n1 = [4, 3, 1, 2]
        n2 = [7, 6, 5, 4, 3, 2, 1]
        n3 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result1 = [2, 3, 1, 4]
        result2 = [1, 2, 3, 4, 5, 6, 7]
        result3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertListEqual(l.sort_fast(n1), result1)
        self.assertListEqual(l.sort_fast(n2), result2)
        self.assertListEqual(l.sort_fast(n3), result3)


if __name__ == '__main__':
    unittest.main()
