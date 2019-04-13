import unittest
import lesson15_bintree as l


class TreeTest(unittest.TestCase):
    """
    1                    8
    2               4        12
    3             2  6    10    14
    4           1 3 5 7  9 11 13 15
    """

    @staticmethod
    def create_tree():
        root = l.BSTNode(8, 'root', None)
        bst = l.BST(root)
        test_list = [8, 4, 12, 2, 6, 1, 3, 5, 7, 10, 14, 9, 11, 13, 15]
        for i in test_list:
            bst.AddKeyValue(i, '{}'.format(i))

        return bst

    def test_add_node(self):
        root = l.BSTNode(8, 'root', None)
        bst = l.BST(root)
        bst.AddKeyValue(4, 'left')
        self.assertFalse(bst.AddKeyValue(4, 'left'))
        self.assertListEqual([i.NodeKey for i in bst.preoder(root)], [8, 4])
        bst.AddKeyValue(6, 'right')
        self.assertListEqual([i.NodeKey for i in bst.preoder(root)], [8, 4, 6])
        self.assertEqual(root.LeftChild.RightChild.NodeKey, 6)
        self.assertEqual(root.LeftChild.LeftChild, None)
        bst.AddKeyValue(2, 'left')
        self.assertEqual(root.LeftChild.LeftChild.NodeKey, 2)
        bst.AddKeyValue(12, 'right')
        self.assertListEqual([i.NodeKey for i in bst.preoder(root)], [8, 4, 2, 6, 12])
        self.assertEqual(root.RightChild.NodeKey, 12)
        bst.AddKeyValue(14, 'right')
        self.assertListEqual([i.NodeKey for i in bst.preoder(root)], [8, 4, 2, 6, 12, 14])
        self.assertEqual(root.RightChild.RightChild.NodeKey, 14)
        self.assertEqual(root.RightChild.LeftChild, None)
        bst.AddKeyValue(15, 'right')
        self.assertListEqual([i.NodeKey for i in bst.preoder(root)], [8, 4, 2, 6, 12, 14, 15])
        self.assertEqual(root.RightChild.RightChild.RightChild.NodeKey, 15)
        self.assertEqual(root.RightChild.RightChild.LeftChild, None)
        bst.AddKeyValue(10, 'left')
        self.assertListEqual([i.NodeKey for i in bst.preoder(root)], [8, 4, 2, 6, 12, 10, 14, 15])
        self.assertEqual(root.RightChild.LeftChild.NodeKey, 10)
        self.assertEqual(root.RightChild.LeftChild.LeftChild, None)
        self.assertEqual(root.RightChild.LeftChild.RightChild, None)
        bst.AddKeyValue(9, 'left')
        self.assertListEqual([i.NodeKey for i in bst.preoder(root)], [8, 4, 2, 6, 12, 10, 9, 14, 15])
        self.assertEqual(root.RightChild.LeftChild.LeftChild.NodeKey, 9)
        self.assertEqual(root.RightChild.LeftChild.RightChild, None)
        bst.AddKeyValue(11, 'right')
        self.assertListEqual([i.NodeKey for i in bst.preoder(root)], [8, 4, 2, 6, 12, 10, 9, 11, 14, 15])
        self.assertEqual(root.RightChild.LeftChild.LeftChild.NodeKey, 9)
        self.assertEqual(root.RightChild.LeftChild.RightChild.NodeKey, 11)
        print([i.NodeKey for i in bst.preoder(root)])

    def test_remove_node(self):
        bst = self.create_tree()

        self.assertFalse(bst.DeleteNodeByKey(100))

        self.assertEqual(bst.Root.LeftChild.LeftChild.LeftChild.NodeKey, 1)
        bst.DeleteNodeByKey(1)
        self.assertEqual(bst.Root.LeftChild.LeftChild.LeftChild, None)

        self.assertEqual(bst.Root.LeftChild.LeftChild.RightChild.NodeKey, 3)
        bst.DeleteNodeByKey(3)
        self.assertEqual(bst.Root.LeftChild.LeftChild.RightChild, None)

        self.assertEqual(bst.Root.LeftChild.RightChild.RightChild.NodeKey, 7)
        bst.DeleteNodeByKey(7)
        self.assertEqual(bst.Root.LeftChild.RightChild.RightChild, None)

        self.assertEqual(bst.Root.LeftChild.RightChild.LeftChild.NodeKey, 5)
        bst.DeleteNodeByKey(5)
        self.assertEqual(bst.Root.LeftChild.RightChild.LeftChild, None)

        bst = self.create_tree()

        self.assertEqual(bst.Root.LeftChild.NodeKey, 4)
        bst.DeleteNodeByKey(4)
        self.assertEqual(bst.Root.LeftChild.NodeKey, 5)
        self.assertEqual(bst.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertEqual(bst.Root.LeftChild.RightChild.NodeKey, 6)
        self.assertEqual(bst.Root.LeftChild.RightChild.LeftChild, None)
        self.assertEqual(bst.Root.LeftChild.Parent.NodeKey, 8)
        self.assertEqual(bst.Root.LeftChild.RightChild.RightChild.NodeKey, 7)

    def test_max_min(self):
        bst = self.create_tree()
        self.assertEqual(bst.FinMinMax(bst.Root, FindMax=True).NodeKey, 15)
        self.assertEqual(bst.FinMinMax(bst.Root, FindMax=False).NodeKey, 1)
        self.assertEqual(bst.FinMinMax(bst.Root.LeftChild, FindMax=True).NodeKey, 7)
        self.assertEqual(bst.FinMinMax(bst.Root.LeftChild, FindMax=False).NodeKey, 1)
        self.assertEqual(bst.FinMinMax(bst.Root.RightChild, FindMax=True).NodeKey, 15)
        self.assertEqual(bst.FinMinMax(bst.Root.RightChild, FindMax=False).NodeKey, 9)
        bst.AddKeyValue(0, 'left')
        self.assertEqual(bst.FinMinMax(bst.Root, FindMax=False).NodeKey, 0)
        print([i.NodeKey for i in bst.GetAllNodes()])


if __name__ == '__main__':
    unittest.main()
