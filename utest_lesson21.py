import copy
import random
import unittest
import lesson21_bubble_selection as l


class InsertSortTest(unittest.TestCase):
    @staticmethod
    def create_test_arrays(n=3):
        for i in range(n):
            yield [random.randint(0, 50) for _ in range(10)]

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

    def test_sort_shell(self):
        n1 = [4, 3, 1, 2]
        n2 = [7, 6, 5, 4, 3, 2, 1]
        n3 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result1 = [1, 2, 3, 4]
        result2 = [1, 2, 3, 4, 5, 6, 7]
        result3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        # print(l.sort_insert(n2, 1))
        self.assertListEqual(l.sort_shell(n1), result1)
        self.assertListEqual(l.sort_shell(n2), result2)
        self.assertListEqual(l.sort_shell(n3), result3)

    def test_SelectionSortStep(self):
        arrays = list(self.create_test_arrays())
        copy_arrays = copy.deepcopy(arrays)

        for index, array in enumerate(arrays):
            for step in range(len(array)):
                l.SelectionSortStep(array, step)
                self.assertEqual(array[step], min(copy_arrays[index][step:]))
                copy_arrays[index] = array.copy()



    def test_BubbleSortStep(self):
        arrays = list(self.create_test_arrays())
        sorted_arrays = [list(sorted(array.copy())) for array in arrays]

        for index, array in enumerate(arrays):
            self.assertTrue(l.BubbleSortStep(array))
            self.assertListEqual(arrays[index], sorted_arrays[index])


if __name__ == '__main__':
    unittest.main()
