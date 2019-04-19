import unittest
import lesson17_heap as l


class TreeTest(unittest.TestCase):

    def test_add(self):
        result1 = [11, 9, 4, 7, 8, 3, 1, 2, 5, 6]
        result2 = [11, 9, 7, 5, 8, 2, 6, 1, 4, 3]
        result3 = [11, 9, 8, 6, 5, 2, 7, 1, 4, 3]
        test_list1 = [11, 9, 4, 7, 8, 3, 1, 2, 5, 6]
        test_list2 = [6, 5, 2, 1, 3, 8, 7, 4, 9, 11]
        test_list3 = [6, 11, 2, 1, 3, 8, 7, 9, 4, 5]

        h1 = l.Heap()
        h1.MakeHeap(test_list1)
        self.assertEqual(h1.HeapArray, result1)
        h2 = l.Heap()
        h2.MakeHeap(test_list2)
        self.assertEqual(h2.HeapArray, result2)
        h3 = l.Heap()
        h3.MakeHeap(test_list3)
        self.assertEqual(h3.HeapArray, result3)
        h3.GetMax()
        h3.GetMax()
        self.assertTrue(h3.Add(100))
        self.assertTrue(h3.Add(101))
        self.assertFalse(h3.Add(103))

    def test_get_max(self):
        h = l.Heap()
        h.MakeHeap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6])
        self.assertEqual(h.GetMax(), 11)
        self.assertListEqual(h.HeapArray, [9, 8, 4, 7, 6, 3, 1, 2, 5])
        self.assertEqual(h.GetMax(), 9)
        self.assertListEqual(h.HeapArray, [8, 7, 4, 5, 6, 3, 1, 2])
        self.assertEqual(h.GetMax(), 8)
        self.assertListEqual(h.HeapArray, [7, 6, 4, 5, 2, 3, 1])
        self.assertEqual(h.GetMax(), 7)
        self.assertListEqual(h.HeapArray, [6, 5, 4, 1, 2, 3])
        self.assertEqual(h.GetMax(), 6)
        self.assertListEqual(h.HeapArray, [5, 3, 4, 1, 2])
        self.assertEqual(h.GetMax(), 5)
        self.assertListEqual(h.HeapArray, [4, 3, 2, 1])
        self.assertEqual(h.GetMax(), 4)
        self.assertListEqual(h.HeapArray, [3, 1, 2])
        self.assertEqual(h.GetMax(), 3)
        self.assertListEqual(h.HeapArray, [2, 1])
        self.assertEqual(h.GetMax(), 2)
        self.assertListEqual(h.HeapArray, [1])
        self.assertEqual(h.GetMax(), 1)
        self.assertListEqual(h.HeapArray, [])


if __name__ == '__main__':
    unittest.main()
