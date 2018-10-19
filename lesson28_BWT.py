from random import randint, shuffle


class Node:
    def __init__(self, colors, flag=None):
        self.left_child_color, self.right_child_color = colors
        self.parent_color = None
        self.id = 0
        if flag:
            self.left_child = None
            self.right_child = None


class Tree:
    def __init__(self, sz):
        self.tree = [Node([None, None]) for _ in range(sz)]

    def add_is_valid(self, index_new_node, new_node):
        parent = (index_new_node - 1) // 2
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2

        if self.tree[0].left_child_color is None:
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

        self.tree[index].left_child_color = node[0]
        self.tree[index].right_child_color = node[1]
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

    def __init__(self, depth=4, count_colors=4):
        self.top_tree = Tree(2 ** depth - 1)
        self.bottom_tree = Tree(2 ** depth - 1)
        self.relationship_trees = []
        self.depth = depth
        self.count_colors = count_colors
        self.id = -1

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
            self.id += 1
            # листьям не раскрашиваем, но запоминаем цвет родителя
            if index * 2 + 1 >= len(tree.tree):
                tree.tree[index] = Node([None, None], flag=True)
                parent = tree.add_is_valid(index, [None, None])[1]
                tree.tree[index].parent_color = parent
                tree.tree[index].id = self.id
                continue

            tree.tree[index].id = self.id
            is_valid = False
            while not is_valid:
                new_node = self.generate_random_colors()
                is_valid = tree.add(index, new_node)

        return tree

    def copy_colors(self, tree1, tree2):
        for index, node in enumerate(tree1.tree):
            self.id += 1
            tree2.tree[index].id = index
            if index * 2 + 1 >= len(tree1.tree):
                tree2.tree[index] = (Node([None, None], flag=True))
                tree2.tree[index].parent_color = node.parent_color
                tree2.tree[index].id = self.id
                continue
            tree2.tree[index].id = self.id
            tree2.tree[index].left_child_color = node.left_child_color
            tree2.tree[index].right_child_color = node.right_child_color
            tree2.tree[index].parent_color = node.parent_color

        return tree2

    def coloring_mirror_tree(self, tree1, tree2):
        self.coloring_random_tree(tree1)
        self.copy_colors(tree1, tree2)
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
        return self.relationship_trees

    def get_node(self, id):
        for node in self.top_tree.tree:
            if node.id == id:
                return node
        for node in self.bottom_tree.tree:
            if node.id == id:
                return node
        return None

    @staticmethod
    def counting_color_in_path(path, color):
        count = 0
        for node in path:
            if node.parent_color == color:
                count += 1
        return count

    def counting_colors_all_paths(self, paths, color):
        count_colors = {}
        for key in paths.keys():
            count_colors[key] = self.counting_color_in_path(paths[key], color)
        return count_colors

    def find_all_paths_tree(self, tree):
        last_level = -2 ** (self.depth - 1)
        paths = {}
        for node in tree.tree[last_level:]:
            path = [node]
            i_node = tree.tree.index(node)
            i_parent = (i_node - 1) // 2

            while i_parent >= 0:
                path.append(tree.tree[i_parent])
                i_parent = (i_parent - 1) // 2
            paths[node] = path[::-1]

        return paths

    def find_all_paths_bwt(self, color):
        paths_top = self.find_all_paths_tree(self.top_tree)
        paths_bottom = self.find_all_paths_tree(self.bottom_tree)

        count_colors_top = self.counting_colors_all_paths(paths_top, color)
        count_colors_bottom = self.counting_colors_all_paths(paths_bottom, color)

        all_paths = []

        for leaf in paths_top:
            # по "левому пути"
            path = paths_top[leaf] + paths_bottom.get(leaf.left_child)[::-1]
            count_colors = count_colors_top.get(leaf) + count_colors_bottom.get(
                leaf.left_child)
            if leaf.left_child_color == color:
                count_colors += 1
            all_paths.append((path, count_colors))
            # по "правому пути"
            path = paths_top[leaf] + paths_bottom.get(leaf.right_child)[::-1]
            count_colors = count_colors_top.get(leaf) + count_colors_bottom.get(
                leaf.right_child)
            if leaf.right_child_color == color:
                count_colors += 1
            all_paths.append((path, count_colors))

        return all_paths

    def optimal_way(self, color, mx=None, mn=None):
        all_paths = self.find_all_paths_bwt(color)

        if mx:
            all_paths.sort(key=lambda x: x[1], reverse=True)
        elif mn:
            all_paths.sort(key=lambda x: x[1])

        return all_paths[0]

    @staticmethod
    def condition_for_step_leaf(tree, leaf, step):

        # left
        if step == 2:
            leaf = leaf.left_child

        # right
        else:
            leaf = leaf.right_child
        return leaf

    def condition_for_step_node(self, tree, node, step):
        left_child = node.id * 2 + 1
        right_child = node.id * 2 + 2

        # parent
        if step == 1:
            if node.parent_color is None:
                return node
            node = tree.tree[(node.id - 1) // 2]

        # left
        elif step == 2:
            # если лист
            if left_child > len(tree.tree) - 1:
                return self.condition_for_step_leaf(tree, node, step)
            node = tree.tree[left_child]

        # right
        else:
            # если лист
            if right_child > len(tree.tree) - 1:
                return self.condition_for_step_leaf(tree, node, step)
            node = tree.tree[right_child]
        return node

    def take_step(self, node, step):
        if node in self.top_tree:
            current_tree = self.top_tree
        else:
            current_tree = self.bottom_tree

        return self.condition_for_step_node(current_tree, node, step)

    def random_walk(self, id):
        current_node = self.top_tree.tree[0]
        count_steps = 0

        while current_node.id != id:
            random_step = randint(1, 3)
            count_steps += 1
            current_node = self.take_step(current_node, random_step)

        return current_node.id, count_steps

    def quantum_walk(self, id):
        nodes = [self.top_tree.tree[0]]
        count_steps = 0

        # while not any([node.id == 39 for node in nodes]):
        while self.bottom_tree.tree[0] not in nodes:

            for i in range(len(nodes)):
                current_node = nodes[i]
                random_step = randint(1, 3)
                first_node = self.take_step(current_node, random_step)
                nodes[i] = first_node

                random_step = randint(1, 3)
                second_node = self.take_step(current_node, random_step)
                nodes.append(second_node)
            count_steps += 1
            print(count_steps)
            print(len(nodes))

        return nodes, count_steps
