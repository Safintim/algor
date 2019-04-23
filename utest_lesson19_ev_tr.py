import unittest
import lesson19_even_trees as l


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

        root = l.SimpleTreeNode(1, None)
        tree = l.SimpleTree(root)

        child1_level2 = l.SimpleTreeNode(6, root)
        child2_level2 = l.SimpleTreeNode(3, root)
        child3_level2 = l.SimpleTreeNode(2, root)

        child1_level3 = l.SimpleTreeNode(8, child1_level2)
        child2_level3 = l.SimpleTreeNode(4, child2_level2)
        child3_level3 = l.SimpleTreeNode(7, child3_level2)
        child4_level3 = l.SimpleTreeNode(5, child3_level2)

        child1_level4 = l.SimpleTreeNode(10, child1_level3)
        child2_level4 = l.SimpleTreeNode(9, child1_level3)

        tree.AddChild(root, child1_level2)
        tree.AddChild(root, child2_level2)
        tree.AddChild(root, child3_level2)

        tree.AddChild(child1_level2, child1_level3)
        tree.AddChild(child2_level2, child2_level3)
        tree.AddChild(child3_level2, child3_level3)
        tree.AddChild(child3_level2, child4_level3)

        tree.AddChild(child1_level3, child1_level4)
        tree.AddChild(child1_level3, child2_level4)

        return tree

    def test_EvenTrees(self):
        tree = self.create_tree()
        self.assertListEqual([node.NodeValue for node in tree.GetAllNodes()], [1, 6, 8, 10, 9, 3, 4, 2, 7, 5])
        self.assertListEqual([node.NodeValue for node in tree.EvenTrees()], [1, 6, 1, 3])

        tree = self.create_tree()
        child1_level2 = tree.Root.Children[0].Children[0]
        child1_level2.Children = []
        child2_level2 = tree.Root.Children[1].Children[0]

        child5_level3 = l.SimpleTreeNode(101, child1_level2)
        child6_level3 = l.SimpleTreeNode(102, child2_level2)

        tree.AddChild(child1_level2, child5_level3)
        tree.AddChild(child2_level2, child6_level3)
        self.assertListEqual([node.NodeValue for node in tree.GetAllNodes()], [1, 6, 8, 101, 3, 4, 102, 2, 7, 5])
        self.assertListEqual([node.NodeValue for node in tree.EvenTrees()], [])

        tree = self.create_tree()
        child1_level2 = tree.Root.Children[0].Children[0]
        child1_level2.Children = []
        child3_level2 = tree.Root.Children[2]
        child3_level2.Children.pop(0)

        child5_level3 = l.SimpleTreeNode(101, child1_level2)
        tree.AddChild(child1_level2, child5_level3)

        self.assertListEqual([node.NodeValue for node in tree.GetAllNodes()], [1, 6, 8, 101, 3, 4, 2, 5])
        self.assertListEqual([node.NodeValue for node in tree.EvenTrees()], [1, 3, 1, 2])

        tree.Root.Children[2].Children = []
        self.assertListEqual([node.NodeValue for node in tree.GetAllNodes()], [1, 6, 8, 101, 3, 4, 2])
        self.assertListEqual([node.NodeValue for node in tree.EvenTrees()], [])

        tree = self.create_tree()
        child3_level2 = tree.Root.Children[2]
        child3_level2.Children = []

        self.assertListEqual([node.NodeValue for node in tree.GetAllNodes()], [1, 6, 8, 10, 9, 3, 4, 2])
        self.assertListEqual([node.NodeValue for node in tree.EvenTrees()], [1, 6, 1, 3])

        tree = self.create_tree()
        child1_level2 = tree.Root.Children[0].Children[0]
        child1_level2.Children = []
        child2_level2 = tree.Root.Children[1].Children[0]
        tree.Root.Children[2].Children = []

        child5_level3 = l.SimpleTreeNode(101, child1_level2)
        child6_level3 = l.SimpleTreeNode(102, child2_level2)

        tree.AddChild(child1_level2, child5_level3)
        tree.AddChild(child2_level2, child6_level3)
        self.assertListEqual([node.NodeValue for node in tree.GetAllNodes()], [1, 6, 8, 101, 3, 4, 102, 2])
        self.assertListEqual([node.NodeValue for node in tree.EvenTrees()], [])



if __name__ == '__main__':
    unittest.main()
