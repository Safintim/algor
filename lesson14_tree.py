class TreeNode:

    def __init__(self, parent, value=None):
        self.parent = parent
        self.child = []
        self.value = value
        self.level = -1


class SimpleTree:

    def __init__(self, root):
        self.root = root

    @staticmethod
    def add_node(parent, node):
        """текущему узлу добавить новый узел в качестве дочернего"""

        parent.child.append(node)
        node.parent = parent
        # node.level = parent.level + 1
        return True

    def remove_child(self, node):
        """
        удаляет узел (не корневой)
        """
        if node != self.root:
            parent = node.parent
            for index, n in enumerate(parent.child, 0):
                # рекурсивно находится нода
                if n == node:
                    # удаляется узел из списка детей родителя
                    parent.child.pop(index)
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
        """ находит все узлы по заданому значению с помощью генератора"""
        result = []
        for node in self.traverse_tree(self.root):
            if node.value == value:
                result.append(node)
        return result

    def move_child(self, start, end):
        """- переместить некорневой узел дочерним узлом в другое место дерева """

        if start != self.root:
            # удаляет из старой позиции и добавляет дочерним элементом в end
            self.remove_child(start)
            self.add_node(end, start)
            return True
        return False

    def count_node(self):
        """считает количество узлов и листьев"""
        count_node = 0
        count_leaf = 0
        for node in self.traverse_tree(self.root):
            # если детей не имеет, то листок
            if not node.child:
                count_leaf += 1
            else:
                count_node += 1
        return count_node, count_leaf

    def set_level(self):
        for n in self.traverse_tree(self.root):
            if n == self.root:
                n.level = 1
            else:
                n.level = n.parent.level + 1
        return