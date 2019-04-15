import unittest
import lesson16_bintreeA as l


class MyTestCase(unittest.TestCase):
    def test_add(self):
        test_list = [8, 4, 12, 2, 6, 1, 3, 5, 7, 10, 14, 9]
        tree = l.aBST(3)

        for i in test_list:
            print(tree.AddKey(i))
        self.assertEqual(tree.AddKey(8), 0)
        self.assertEqual(tree.AddKey(2), 3)
        self.assertEqual(tree.AddKey(11), 12)
        self.assertEqual(tree.AddKey(13), 13)
        self.assertEqual(tree.AddKey(15), 14)

        self.assertEqual(tree.AddKey(100), -1)
        self.assertEqual(tree.AddKey(10), 5)
        self.assertEqual(tree.AddKey(12), 2)


if __name__ == '__main__':
    unittest.main()
