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
            else:
                index = 2 * index + 2
            if index > len(self.tree):
                return None

            if self.tree[index] is None:
                return -index
            return self.find(node, index)

    def add(self, node):
        index = self.find(node)
        if index is None:
            return 'выход за границы'
        elif index <= 0:
            self.tree[abs(index)] = node
        else:
            return 'Нода уже есть'

    def __iter__(self):
        return iter(self.tree)


# test_list = [8, 4, 12, 2, 6, 1, 3, 5, 7, 10, 14, 9, 11, 13, 15]
# tree = Tree2(len(test_list))
# for i in test_list:
#     tree.add(i)
#
# print(tree.tree)  # [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
# for i in tree:
#     print(i)


class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = sum(2**i for i in range(depth+1))
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):

        if not self.Tree[0]:
            return 0

        i = 0

        while i < len(self.Tree):
            if self.Tree[i] == key:
                return i
            elif self.Tree[i] > key:
                index = 2 * i + 1
            else:
                index = 2 * i + 2

            if index > len(self.Tree):
                break
            if self.Tree[index] is None:
                return -index

            i = index

        return None  # не найден

    def AddKey(self, key):
        index = self.FindKeyIndex(key)

        if index is None:
            return -1
        elif index <= 0:
            self.Tree[abs(index)] = key

        return index
