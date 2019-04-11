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

        root = l.SimpleTreeNode(None, 9)
        tree = l.SimpleTree(root)

        child1 = l.SimpleTreeNode(root, 4)
        child2 = l.SimpleTreeNode(root, 17)

        child3 = l.SimpleTreeNode(child1, 3)
        child4 = l.SimpleTreeNode(child1, 6)
        child5 = l.SimpleTreeNode(child1, 90)
        child6 = l.SimpleTreeNode(child2, 22)

        child7 = l.SimpleTreeNode(child6, 20)
        child8 = l.SimpleTreeNode(child5, 51)
        child11 = l.SimpleTreeNode(child4, 105)

        child9 = l.SimpleTreeNode(child8, 1)
        child10 = l.SimpleTreeNode(child8, 2)
        child12 = l.SimpleTreeNode(child10, 90)

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
        temp = tree.root.Children[0]
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
        self.assertListEqual(list(i.NodeValue for i in temp[0].Children), result1)
        self.assertEqual(len(temp), 1)
        self.assertEqual(list(i.NodeValue for i in temp), [4])

    def test_find_childs(self):
        tree = self.create_tree()

        self.assertListEqual(list(i.NodeValue for i in tree.FindNodesByValue(1)), [1])
        self.assertListEqual(list(i.NodeValue for i in tree.FindNodesByValue(90)), [90, 90])

    def test_size(self):
        root = l.SimpleTreeNode(None, 9)
        tree = l.SimpleTree(root)
        print(len(tree.GetAllNodes()))
        self.assertEqual(len(tree.GetAllNodes()), 1)
        self.assertEqual(tree.Count(), 1)
        self.assertEqual(tree.LeafCount(), 1)
        tree = self.create_tree()
        self.assertEqual(len(tree.GetAllNodes()), 13)

    def test_move_child(self):
        tree = self.create_tree()
        temp = tree.Root.Children
        tree.MoveNode(temp[1], temp[0])
        self.assertListEqual(list(i.NodeValue for i in temp[0].Children), [3, 6, 90, 17])
        self.assertListEqual(list(i.NodeValue for i in temp[0].Children[3].Children), [22])

    def test_count_node(self):
        tree = self.create_tree()
        count_leaf = 5
        count_node = 8
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
