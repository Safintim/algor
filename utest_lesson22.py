import unittest
import lesson22_sort_fast as l


class FastSortTest(unittest.TestCase):

    def test_sort_fast(self):
        n1 = [4, 3, 1, 2]
        n2 = [7, 6, 5, 4, 3, 2, 1]
        n3 = [8, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 8, 8]
        result1 = [2, 3, 1, 4]
        result2 = [1, 2, 3, 4, 5, 6, 7]
        result3 = [8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 8, 8]
        self.assertListEqual(l.sort_fast(n1)[0], result1)
        self.assertListEqual(l.sort_fast(n2)[0], result2)
        self.assertListEqual(l.sort_fast(n3)[0], result3)

    def test_sort_fast2(self):
        n1 = [4, 3, 1, 2]
        n2 = [7, 6, 5, 4, 3, 2, 1]
        n3 = [8, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 8, 8]
        result1 = l.sort_fast(n1)
        result2 = l.sort_fast(n2)
        result3 = l.sort_fast(n3)

        self.assertEqual(result1[1], 1)
        self.assertEqual(result1[2], 2)
        self.assertEqual(result2[1], 3)
        self.assertEqual(result2[2], 4)
        self.assertEqual(result3[1], 8)
        self.assertEqual(result3[2], 9)


if __name__ == '__main__':
    unittest.main()
