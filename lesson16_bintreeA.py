"""Бинарное дерево в виде массива"""


class Tree2:

    def __init__(self, sz):

        self.tree = [None] * sz

    def find(self, node, i=0):

        if self.tree[0] is None:
            return 0

        for index in range(i, len(self.tree)):
            if self.tree[index] == node:
                return index
            elif self.tree[index] > node:
                index = 2 * index + 1
                if self.tree[index] is None:
                    return -index
                return self.find(node, index)
            else:
                index = 2 * index + 2
                if self.tree[index] is None:
                    return -index
                return self.find(node, index)

    def add(self, node):
        index = self.find(node)
        if index <= 0:
            self.tree[abs(index)] = node
        else:
            print('Нода уже есть')

    def __iter__(self):
        return iter(self.tree)


test_list = [8, 4, 12, 2, 6, 1, 3, 5, 7, 10, 14, 9, 11, 13, 15]
tree = Tree2(len(test_list))
for i in test_list:
    tree.add(i)

print(tree.tree)  # [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
for i in tree:
    print(i)