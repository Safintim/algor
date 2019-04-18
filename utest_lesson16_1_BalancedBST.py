import unittest
import lesson16_1_check as l


class MyTestCase(unittest.TestCase):
    def pre_order(self, node):
        yield node
        if node.LeftChild:
            yield from self.pre_order(node.LeftChild)
        if node.RightChild:
            yield from self.pre_order(node.RightChild)



    def test_CreateFromArray(self):
        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.CreateFromArray(a)
        print([(i) for i in bst.BSTArray])

    def test_GenerateTree(self):
        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.CreateFromArray(a)
        bst.GenerateTree()

    def test_balanced(self):
        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.CreateFromArray(a)
        bst.GenerateTree()
        self.assertEqual(bst.IsBalanced(bst.Root), True)
        bst.Root.LeftChild = None
        self.assertEqual(bst.IsBalanced(bst.Root), False)

        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.CreateFromArray(a)
        bst.GenerateTree()

        bst.Root.LeftChild.LeftChild = None
        bst.Root.LeftChild.RightChild = None
        self.assertEqual(bst.IsBalanced(bst.Root), False)

        a = [7, 6, 4, 9, 5, 14, 15, 2, 11, 8, 13, 1, 3, 12, 10]
        bst = l.BalancedBST()
        bst.CreateFromArray(a)
        bst.GenerateTree()

        bst.Root.LeftChild.LeftChild.LeftChild = None
        bst.Root.LeftChild.LeftChild.RightChild = None
        self.assertEqual(bst.IsBalanced(bst.Root), True)

if __name__ == '__main__':
    unittest.main()
