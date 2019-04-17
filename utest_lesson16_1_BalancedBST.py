import unittest
import lesson16_1_check as l


class MyTestCase(unittest.TestCase):
    def test_CreateFromArray(self):
        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.CreateFromArray(a)
        print([(i.NodeKey,i.Level) for i in bst.BSTArray])

    def test_GenerateTree(self):
        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.CreateFromArray(a)
        bst.GenerateTree()
        print()

if __name__ == '__main__':
    unittest.main()
