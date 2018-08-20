import unittest
import random as r
import lesson23_sort_line as l


class TestSort(unittest.TestCase):
    def test_line_sort(self):
        test_list = [chr(r.randint(97, 104)) + str(r.randint(0, 9)) + str(r.randint(0, 9)) for i in range(500)]
        test_list1 = test_list.copy()
        test_list.sort()

        test_list2 = ['a01', 'b64', 'g99', 'a00', 'b63', 'b65']
        result2 = ['a00', 'a01', 'b63', 'b64', 'b65', 'g99']
        self.assertListEqual(l.ksort(test_list2, 800), result2)
        self.assertListEqual(l.ksort(test_list1, 800), test_list)


if __name__ == '__main__':
    unittest.main()
