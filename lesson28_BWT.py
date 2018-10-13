from random import randint, shuffle

"""
Элемент дерева хранит список цветов = [left_child_color, right_child]
"""


class Node:
    def __init__(self, colors, flag=None):
        self.left_child_color, self.right_child_color = colors
        self.parent_color = None
        self.colors = colors
        if flag:
            self.left_child = None
            self.right_child = None


class Tree:
    def __init__(self, sz):
        self.tree = [None] * sz

    def add_is_valid(self, index_new_node, new_node):
        parent = (index_new_node - 1) // 2
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2

        if self.tree[0] is None:
            return True, None

        elif left_child == index_new_node:
            if self.tree[parent].left_child_color in new_node:
                return False, None
            else:
                return True, self.tree[parent].left_child_color
        elif right_child == index_new_node:
            if self.tree[parent].right_child_color in new_node:
                return False, None
            else:
                return True, self.tree[parent].right_child_color

    def add(self, index, node):
        temp = self.add_is_valid(index, node)
        add_is_valid = temp[0]
        if not add_is_valid:
            return False
        self.tree[index] = Node(node)
        self.tree[index].parent_color = temp[1]
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

    def __init__(self, depth=3, count_colors=4):
        self.top_tree = Tree(2 ** depth - 1)
        self.bottom_tree = Tree(2 ** depth - 1)
        self.relationship_trees = []
        self.depth = depth
        self.count_colors = count_colors

    def generate_random_colors(self, exclude=[]):
        colors = set()
        while len(colors) < 2:
            color = randint(1, self.count_colors)
            if color in exclude:
                continue
            colors.add(color)
        return list(colors)

    def coloring_random_tree(self, tree):
        for index, node in enumerate(tree.tree):
            # листьям не раскрашиваем, но запоминаем цвет родителя
            if index * 2 + 1 >= len(tree.tree):
                tree.tree[index] = Node([None, None], flag=True)
                parent = tree.add_is_valid(index, [None, None])[1]
                tree.tree[index].parent_color = parent
                continue

            is_valid = False
            while not is_valid:
                new_node = self.generate_random_colors()
                is_valid = tree.add(index, new_node)

        return tree

    def coloring_mirror_tree(self, tree1, tree2):
        tree1 = self.coloring_random_tree(tree1)
        tree2.tree = tree1.tree.copy()
        return tree1, tree2

    def create_tree(self, tree):
        """тестовая функция"""
        return self.coloring_random_tree(tree)

    def bind_trees(self, tree1, tree2):
        last_level = -2 ** (self.depth - 1)

        top_tree = tree1.tree[last_level:]
        bottom_tree = tree2.tree[last_level:]

        while None in [i.right_child for i in top_tree] or\
                None in [i.right_child for i in bottom_tree]:

            shuffle(top_tree)
            shuffle(bottom_tree)

            for index in range(len(top_tree)):
                exclude = [top_tree[index].parent_color,
                           bottom_tree[index].parent_color]
                colors = self.generate_random_colors(exclude=exclude)

                top_tree[index].left_child = bottom_tree[index]
                top_tree[index].left_child_color = colors[0]
                top_tree[index].right_child_color = colors[1]

                bottom_tree[index].left_child = top_tree[index]
                bottom_tree[index].left_child_color = colors[0]
                bottom_tree[index].right_child_color = colors[1]

            for node_top in top_tree:
                for node_bottom in bottom_tree:
                    if node_top.right_child_color == node_bottom.right_child_color:
                        if node_top.left_child != node_bottom and \
                                node_bottom.left_child != node_top:
                            node_top.right_child = node_bottom
                            node_bottom.right_child = node_top
                            break

        self.relationship_trees = tree1.tree[last_level:] + tree2.tree[last_level:]
        # return tree1.tree[-2 ** (self.depth - 1):],
        #  tree2.tree[-2 ** (self.depth - 1):]
        return self.relationship_trees


