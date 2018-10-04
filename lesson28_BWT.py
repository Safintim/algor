from random import randint
from collections import namedtuple

"""
Элемент дерева хранит список цветов = [left_child_color, right_child]
"""


class Tree:
    def __init__(self):
        self.tree = []

    def add_is_valid(self, new_node):
        parent = (len(self.tree) - 1) // 2
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2
        index_new_node = len(self.tree)

        left = 0
        right = 1

        if not self.tree:
            return True
        elif left_child == index_new_node:
            if self.tree[parent][left] in new_node:
                return False
        elif right_child == index_new_node:
            if self.tree[parent][right] in new_node:
                return False

        return True

    def add(self, node):
        if not self.add_is_valid(node):
            return False
        self.tree.append(node)
        return True

    def __iter__(self):
        return iter(self.tree)


class BWT:
    COLORS = {
        1: 'green',
        2: 'blue',
        3: 'red',
        4: 'purple'
    }

    def __init__(self, depth=4, count_colors=4):
        self.top_tree = Tree()
        self.bottom_tree = Tree()
        self.relationship_trees = []
        self.depth = depth
        self.count_colors = count_colors

    def generate_random_colors(self):
        colors = set()
        while len(colors) < 2:
            color = randint(1, self.count_colors)
            colors.add(color)

        return list(colors)

    def coloring_random_tree(self, tree):
        for count in range(2 ** self.depth - 1):
            is_valid = False
            while not is_valid:
                new_node = self.generate_random_colors()
                is_valid = tree.add(new_node)

        return tree

    def coloring_mirror_tree(self, tree1, tree2):
        self.coloring_random_tree(tree1)
        tree2 = tree1.copy()

        return tree1, tree2

    def create_tree(self, tree):
        """тестовая функция"""
        return self.coloring_random_tree(tree)

    def bind_trees(self):
        pass
