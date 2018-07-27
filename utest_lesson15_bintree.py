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
        bin_tree = l.Tree2()
        test_list = [8, 4, 12, 2, 6, 1, 3, 5, 7, 10, 14, 9, 11, 13, 15]
        for i in test_list:
            bin_tree.add_node(l.TreeNode2(None, i))

        return bin_tree

    def test_add_node(self):
        bin_tree = self.create_tree()
        result = [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]
        self.assertListEqual(list(i.key for i in bin_tree.preoder(bin_tree.root)), result)

    def test_remove_node(self):
        bin_tree = self.create_tree()
        result = [8, 4, 2, 1, 3, 6, 5, 7, 13, 10, 9, 11, 14, 15]
        r12 = bin_tree.root.right_child
        bin_tree.remove_node(r12)
        self.assertListEqual(list(i.key for i in bin_tree.preoder(bin_tree.root)), result)
        self.assertEqual(bin_tree.find(12).is_key, False)

    def test_find(self):
        bin_tree = self.create_tree()
        temp1 = bin_tree.find(0)
        bin_tree.current = bin_tree.root
        temp2 = bin_tree.find(14)
        self.assertListEqual([temp1.node.key, temp1.is_key, temp1.direct], [1, False, 'left'])
        self.assertListEqual([temp2.node.key, temp2.is_key, temp2.direct], [14, True, None])

    def test_max(self):
        bin_tree = self.create_tree()
        r4 = bin_tree.root.left_child
        self.assertEqual(bin_tree.max(bin_tree.root).key, 15)
        self.assertEqual(bin_tree.max(r4).key, 7)

    def test_min(self):
        bin_tree = self.create_tree()
        r12 = bin_tree.root.right_child
        self.assertEqual(bin_tree.min(bin_tree.root).key, 1)
        self.assertEqual(bin_tree.min(r12).key, 9)


if __name__ == '__main__':
    unittest.main()
