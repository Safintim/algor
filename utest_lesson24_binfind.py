import unittest
import random as r
import lesson24_bin_find as l


class TestSort(unittest.TestCase):
    def test_bin_find(self):
        test_list = [10, 15, 65, 76, 77, 82, 97]
        result1 = 1
        result2 = -1
        self.assertEqual(l.bin_find(test_list, 15), result1)
        self.assertEqual(l.bin_find(test_list, 83), result2)


if __name__ == '__main__':
    unittest.main()
