import unittest
import lesson9_hash as l


class HashTest(unittest.TestCase):

    def test_put(self):
        test_list = [3, 93, 60, 25, 73, 83, 45, 29, 18, 8, 28, 48, 40, 88, 0, 32, 15]
        result_list = [3, 48, 15, 25, 73, 83, 93, 40, 45, 18, 88, 29, 8, 0, 60, 28, 32]
        h = l.HashTable(17, 3)

        for i in test_list:
            h.put(i)

        self.assertListEqual(result_list, h.slots)

    def test_find(self):
        test_list = [3, 93, 60, 25, 73, 83, 45, 29, 18, 8, 28, 48, 40, 88, 0, 32, 15]
        h1 = l.HashTable(17, 3)
        h2 = l.HashTable(17, 3)
        for i in test_list:
            h1.put(i)
        for i in test_list[::-1]:
            h2.put(i)
        index1 = h1.find(93)
        index2 = h2.find(93)
        self.assertEqual(h1.slots[index1], 93)
        self.assertEqual(h2.slots[index2], 93)
        self.assertEqual(index1, 6)
        self.assertEqual( h2.find(30), None)


if __name__ == '__main__':
    unittest.main()
