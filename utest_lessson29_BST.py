import unittest
import lesson29_BST as l


class MyTestCase(unittest.TestCase):

    def test_halve_arr(self):
        test_list = [12, 7, 4, 14, 5, 11, 5]
        test_list.sort()  # [4, 5, 5, 7, 11, 12, 14]
        result = [
            [4, 5, 5, 7, 11, 12, 14],
            [4, 5, 5], [11, 12, 14],
            [4], [5], [11], [14]
        ]
        bst = l.BST(h=2)

        self.assertEqual(bst.halve_arr(test_list), result)

    def test_add(self):
        test_list = [12, 7, 4, 14, 5, 11, 5]
        result = [7, 5, 12, 4, 5, 11, 14]
        bst = l.BST(h=2)
        bst.add(test_list)

        self.assertEqual(bst.tree, result)


if __name__ == '__main__':
    unittest.main()
