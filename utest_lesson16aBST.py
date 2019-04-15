import unittest
import lesson16_bintreeA as l

class MyTestCase(unittest.TestCase):
    def test_add(self):
        test_list = [8, 4, 12, 2, 6, 1, 3, 5, 7, 10, 14, 9, 11, 13, 15]
        tree = l.aBST(3)
        self.assertEqual(len(tree.Tree), len(test_list))

        for i in test_list:
            print(tree.AddKey(i))

        self.assertEqual(tree.AddKey(100), -1)
        self.assertEqual(tree.AddKey(10), 5)


if __name__ == '__main__':
    unittest.main()
