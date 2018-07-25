class TreeNode:

    def __init__(self, parent, value=None):
        self.parent = parent
        self.child = []
        self.value = value
        self.level = -1

    def add_child(self, node):
        self.child.append(node)


class SimpleTree:

    def __init__(self, root):
        self.root = root
        self.current = self.root

    def add_node(self, node):
        # текущему узлу добавить новый узел в качестве дочернего
        self.current.add_child(node)
        return True

    def remove_child(self, node):
        if node != self.root:
            parent = node.parent
            for i, n in enumerate(parent.child, 0):
                if n == node:
                    parent.child.pop(i)
                    return True
        else:
            return False

    def traverse_tree(self, node):
        yield node
        for ch in node.child:
            yield from self.traverse_tree(ch)

    def __iter__(self):
        return self

    def find_childs(self, value):
        # находит все узлы по заданому значению
        # с помощью генератора
        result = []
        for node in self.traverse_tree(self.root):
            if node.value == value:
                result.append(node)
        return result

    def move_child(self, start, end):
        # - переместить некорневой узел дочерним узлом в другое
        # место дерева

        return

    def count_node(self):
        # считает количество узлов и листьев
        count_node = 0
        count_leaf = 0
        for node in self.traverse_tree(self.root):
            if not node.child:
                count_leaf += 1
            else:
                count_node += 1
        return count_node, count_leaf

    def set_level(self):
        # каджому узлу устанавливает уровень вложенности
        return


root = TreeNode(None, 9)
tree = SimpleTree(root)

child1 = TreeNode(root, 4)
child2 = TreeNode(root, 17)

child3 = TreeNode(child1, 3)
child4 = TreeNode(child1, 6)
child5 = TreeNode(child2, 22)


tree.add_node(child1)
tree.add_node(child2)

child1.add_child(child3)
child1.add_child(child4)
child2.add_child(child5)

# print(tree.remove_child(child5))

tree.find_childs(3)
# tree.set_level()
for i in tree.traverse_tree(root):
    print(i.value, i.level)

# print(tree.find_childs(3)[0].value)

print(tree.count_node())