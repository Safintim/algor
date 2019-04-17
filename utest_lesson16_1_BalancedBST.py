import unittest
import lesson16_1_check as l


class MyTestCase(unittest.TestCase):
    def pre_order(self, node):
        yield node
        if node.LeftChild:
            yield from self.pre_order(node.LeftChild)
        if node.RightChild:
            yield from self.pre_order(node.RightChild)

    def go_left(self, FromNode):
        while FromNode.LeftChild:
            yield FromNode
            FromNode = FromNode.LeftChild

        yield FromNode

    def go_right(self, FromNode):
        while FromNode.RightChild:
            yield FromNode
            FromNode = FromNode.RightChild

        yield FromNode

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

        self.assertEqual(len([i for i in self.go_left(bst.Root)]), len([i for i in self.go_right(bst.Root)]))
        print([i.NodeKey for i in self.pre_order(bst.Root)])


if __name__ == '__main__':
    unittest.main()
