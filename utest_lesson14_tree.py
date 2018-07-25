import unittest
import lesson14_tree as l


class TreeTest(unittest.TestCase):
    """
    1                    9
    2                4      17
    3             3  6  90    22
    4               105   51   20
    5                   1   2
    """

    @staticmethod
    def create_tree():

        root = l.TreeNode(None, 9)
        tree = l.SimpleTree(root)

        child1 = l.TreeNode(root, 4)
        child2 = l.TreeNode(root, 17)

        child3 = l.TreeNode(child1, 3)
        child4 = l.TreeNode(child1, 6)
        child5 = l.TreeNode(child1, 90)
        child6 = l.TreeNode(child2, 22)

        child7 = l.TreeNode(child6, 20)
        child8 = l.TreeNode(child5, 51)
        child11 = l.TreeNode(child4, 105)

        child9 = l.TreeNode(child8, 1)
        child10 = l.TreeNode(child8, 2)

        tree.add_node(child1)
        tree.add_node(child2)
        tree.add_node(child3)
        tree.add_node(child4)
        tree.add_node(child5)
        tree.add_node(child6)
        tree.add_node(child7)
        tree.add_node(child8)
        tree.add_node(child9)
        tree.add_node(child10)
        tree.add_node(child11)
        return tree

    def test_add_child(self):
        tree = self.create_tree()
        result1 = [3, 6, 90]
        result2 = [1, 2]
        temp = tree.root.child[0]
        self.assertListEqual(list(i.value for i in temp.child[2].child[0].child),result2)
        self.assertListEqual(list(i.value for i in temp.child), result1)

    def test_remove_child(self):
        tree = self.create_tree()
        result1 = [6, 90]
        temp = tree.root.child
        node1 = temp[0].child[0]
        node2 = temp[1]

        tree.remove_child(node1)
        tree.remove_child(node2)
        self.assertListEqual(list(i.value for i in temp[0].child), result1)
        self.assertEqual(len(temp), 1)

    def test_find_childs(self):
        tree = self.create_tree()
        result = [90]
        # result2 = [1, 1, 1]
        # self.assertListEqual(list(i.value for i in tree.find_childs(1)), result2)
        self.assertListEqual(list(i.value for i in tree.find_childs(90)), result)

    def test_move_child(self):
        tree = self.create_tree()
        temp = tree.root.child
        result1 = [3, 6, 90, 17]
        result2 = [22]
        tree.move_child(temp[1], temp[0])
        self.assertListEqual(list(i.value for i in temp[0].child), result1)
        self.assertListEqual(list(i.value for i in temp[0].child[3].child), result2)

    def test_count_node(self):
        tree = self.create_tree()
        count_leaf = 5
        count_node = 7
        temp = tree.count_node()

        self.assertEqual(temp[0], count_node)
        self.assertEqual(temp[1], count_leaf)

    def test_set_level(self):
        tree = self.create_tree()
        tree.set_level()
        result = 5

        self.assertEqual(tree.find_childs(1)[0].level, result)

if __name__ == '__main__':
    unittest.main()
