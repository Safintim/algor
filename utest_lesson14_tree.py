import unittest
import lesson14_tree as l


class TreeTest(unittest.TestCase):
    """
    1                    9
    2                4      17
    3             3  6  90    22
    4               105   51   20
    5                   1   2
    6                      90
    """

    @staticmethod
    def create_tree():

        root = l.SimpleTreeNode(9, None)
        tree = l.SimpleTree(root)

        child1 = l.SimpleTreeNode(4, root)
        child2 = l.SimpleTreeNode(17, root)

        child3 = l.SimpleTreeNode(3, child1)
        child4 = l.SimpleTreeNode(6, child1)
        child5 = l.SimpleTreeNode(90, child1)
        child6 = l.SimpleTreeNode(22, child2)

        child7 = l.SimpleTreeNode(20, child6)
        child8 = l.SimpleTreeNode(51, child5)
        child11 = l.SimpleTreeNode(105, child4)

        child9 = l.SimpleTreeNode(1, child8)
        child10 = l.SimpleTreeNode(2, child8)
        child12 = l.SimpleTreeNode(90, child10)

        tree.AddChild(root, child1)
        tree.AddChild(root, child2)
        tree.AddChild(child1, child3)
        tree.AddChild(child1, child4)
        tree.AddChild(child1, child5)
        tree.AddChild(child4, child11)
        tree.AddChild(child2, child6)
        tree.AddChild(child6, child7)
        tree.AddChild(child5, child8)
        tree.AddChild(child8, child9)
        tree.AddChild(child8, child10)
        tree.AddChild(child10, child12)
        return tree

    def test_add_child(self):
        tree = self.create_tree()
        result1 = [3, 6, 90]
        result2 = [1, 2]
        temp = tree.Root.Children[0]
        self.assertListEqual(list(i.NodeValue for i in temp.Children[2].Children[0].Children), result2)
        self.assertListEqual(list(i.NodeValue for i in temp.Children), result1)

    def test_remove_child(self):
        tree = self.create_tree()
        result1 = [6, 90]
        temp = tree.Root.Children
        node1 = temp[0].Children[0]
        node2 = temp[1]
        tree.DeleteNode(node1)
        tree.DeleteNode(node2)
        # print([i.NodeValue for i in tree.GetAllNodes()])
        self.assertEqual(len(tree.Root.Children), 1)
        self.assertListEqual(list(i.NodeValue for i in temp[0].Children), result1)
        self.assertEqual(len(temp), 1)
        self.assertEqual(list(i.NodeValue for i in temp), [4])
        root = l.SimpleTreeNode(9, None)
        tree = l.SimpleTree(root)
        tree.DeleteNode(root)
        self.assertEqual(tree.GetAllNodes(), [root])

        child1 = l.SimpleTreeNode(4, None)
        tree.AddChild(root, child1)
        tree.DeleteNode(child1)
        self.assertEqual(tree.GetAllNodes(), [root])

        child1 = l.SimpleTreeNode(4, root)
        child2 = l.SimpleTreeNode(17, root)
        other_node = l.SimpleTreeNode(53, None)
        tree.AddChild(root, child1)
        tree.AddChild(root, child2)
        tree.DeleteNode(child1)
        tree.DeleteNode(other_node)
        self.assertEqual(tree.GetAllNodes(), [root, child2])

        tree = self.create_tree()
        tree.DeleteNode(tree.Root.Children[0])
        tree.DeleteNode(tree.Root.Children[0])
        self.assertEqual(tree.GetAllNodes(), [tree.Root])

    def test_find_childs(self):
        tree = self.create_tree()
        t = tree.Root.Children[0].Children[2].Children[0].Children[0]
        # print(t.NodeValue)
        self.assertListEqual(tree.FindNodesByValue(4), [tree.Root.Children[0]])
        self.assertListEqual(tree.FindNodesByValue(1), [t])
        self.assertListEqual([i.NodeValue for i in tree.FindNodesByValue(90)], [90, 90])

        root = l.SimpleTreeNode(9, None)
        tree = l.SimpleTree(root)
        self.assertListEqual(tree.FindNodesByValue(9), [root])
        self.assertListEqual([i.NodeValue for i in tree.FindNodesByValue(9)], [9])

    def test_size(self):
        root = l.SimpleTreeNode(9, None)
        tree = l.SimpleTree(root)
        self.assertEqual(len(tree.GetAllNodes()), 1)
        self.assertEqual(tree.Count(), 1)
        self.assertEqual(tree.LeafCount(), 1)
        tree = self.create_tree()
        self.assertEqual(len(tree.GetAllNodes()), 13)
        self.assertEqual(tree.LeafCount(), 5)

    def test_move_child(self):
        tree = self.create_tree()
        temp = tree.Root.Children
        tree.MoveNode(temp[1], temp[0])
        self.assertListEqual(list(i.NodeValue for i in temp[0].Children), [3, 6, 90, 17])
        self.assertListEqual(list(i.NodeValue for i in temp[0].Children[3].Children), [22])

    def test_count_node(self):
        tree = self.create_tree()
        count_leaf = 5
        count_node = 13
        temp = tree.Count()
        temp2 = tree.LeafCount()
        self.assertEqual(temp, count_node)
        self.assertEqual(temp2, count_leaf)

    def test_set_level(self):
        tree = self.create_tree()
        tree.set_level()
        result = 5

        self.assertEqual(tree.FindNodesByValue(1)[0].level, result)


if __name__ == '__main__':
    unittest.main()
