import unittest
import lesson21_sort_insert as l


class InsertSortTest(unittest.TestCase):

    def test_sort_insert(self):
        n1 = [4, 3, 1, 2]
        n2 = [7, 6, 5, 4, 3, 2, 1]
        n22 = n2.copy()
        result1 = [1, 2, 3, 4]
        result2 = [1, 2, 3, 4, 5, 6, 7]
        result3 = [1, 3, 2, 4, 6, 5, 7]
        # print(l.sort_insert(n2, 1))
        self.assertListEqual(l.sort_insert(n1, 1), result1)
        self.assertListEqual(l.sort_insert(n2, 1), result2)
        self.assertListEqual(l.sort_insert(n22, 3), result3)


if __name__ == '__main__':
    unittest.main()
