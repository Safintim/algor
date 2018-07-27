from collections import namedtuple


class TreeNode2:

    def __init__(self, parent, key):
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.key = key


class Tree2:

    def __init__(self):
        self.root = None
        self.current = self.root
        self.result_find = namedtuple('result_find', ['node', 'is_key', 'direct'])

    def preoder(self, root):
        yield root
        if root.left_child:
            yield from self.preoder(root.left_child)
        if root.right_child:
            yield from self.preoder(root.right_child)

    def __iter__(self):
        return self

    def find(self, key):
        # по сути это проверка только, когда дерево пусто
        if self.current is None:
            return self.result_find(self.current, False, None)
            # return [self.current, False, None]
        # если нашлась нода с таким же ключом
        elif self.current.key == key:
            return self.result_find(self.current, True, None)
            # return [self.current, True, None]
        elif key < self.current.key:
            '''если справа или слева пусто, то нужно запомнить родителя, чтобы после добавить к нему ноду'''
            if self.current.left_child is None:
                return self.result_find(self.current, False, 'left')
                # return [self.current, False, 'left']
            self.current = self.current.left_child
            return self.find(key)
        else:
            # key > self.current.key:
            if self.current.right_child is None:
                return self.result_find(self.current, False, 'right')
                # return [self.current, False, 'right']
            self.current = self.current.right_child
            return self.find(key)

    def add_node(self, n):
        f = self.find(n.key)
        # с индексами работать не особо удобно
        # node = f[0]
        # is_key = f[1]
        # direct = f[2]

        if f.node is None:
            self.root = n
        elif f.is_key:
            print('Такой ключ уже есть')
        else:
            if f.direct == 'right':
                f.node.right_child = n
                n.parent = f.node
            else:
                f.node.left_child = n
                n.parent = f.node
        self.current = self.root

    def max(self, node):
        f = self.find(node.key)
        self.current = self.root
        if f.is_key:
            temp = f.node.right_child
            while True:
                if temp.right_child is None:
                    return temp
                temp = temp.right_child
        else:
            print('Такой ноды нет')

    def min(self, node):
        f = self.find(node.key)
        self.current = self.root
        if f.is_key:
            temp = f.node.left_child
            while True:
                if temp.left_child is None:
                    return temp
                temp = temp.left_child
        else:
            print('Такой ноды нет')

    def remove_node(self, node):
        f = self.find(node.key)
        self.current = self.root
        if f.is_key:
            # минимальный "справа"
            min_node = self.min(f.node.right_child)
            # родителю минимального приемника левому ребру None
            min_node.parent.left_child = None
            # установить новому узлу "лево и право"
            min_node.left_child = f.node.left_child
            min_node.right_child = f.node.right_child
            # родителю удаляемого узла задать нового приемника
            f.node.parent.right_child = min_node
        else:
            print('Такой ноды нет')
