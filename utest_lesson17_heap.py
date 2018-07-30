import unittest
import lesson_17_heap as l


class TreeTest(unittest.TestCase):

    def test_add(self):
        result1 = [11, 9, 4, 7, 8, 3, 1, 2, 5, 6]
        result2 = [11, 9, 7, 5, 8, 2, 6, 1, 4, 3]
        result3 = [11, 9, 8, 6, 5, 2, 7, 1, 4, 3]
        test_list1 = [11, 9, 4, 7, 8, 3, 1, 2, 5, 6]
        test_list2 = [6, 5, 2, 1, 3, 8, 7, 4, 9, 11]
        test_list3 = [6, 11, 2, 1, 3, 8, 7, 9, 4, 5]

        h1 = l.Heap()
        for i in test_list1:
            h1.add(i)
        h2 = l.Heap()
        for i in test_list2:
            h2.add(i)

        h3 = l.Heap()
        for i in test_list3:
            h3.add(i)

        self.assertListEqual(h1.heap, result1)
        self.assertListEqual(h2.heap, result2)
        self.assertListEqual(h3.heap, result3)

    def test_remove_max(self):
        h = l.Heap()
        h.heap = [11, 9, 4, 7, 8, 3, 1, 2, 5, 6]
        h.remove_max()
        h.remove_max()
        h.remove_max()
        self.assertListEqual(h.heap, [7, 6, 4, 5, 2, 3, 1])


if __name__ == '__main__':
    unittest.main()
