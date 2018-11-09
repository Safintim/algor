"""1 способ"""


class BST:
    def __init__(self, h):
        self.tree = [None] * (pow(2, h+1) - 1)

    @staticmethod
    def halve_arr(arr):
        halves_arr = [arr]

        for half in halves_arr:
            if half[:len(half) // 2]:
                halves_arr.append(half[:len(half) // 2])
                halves_arr.append(half[len(half) // 2 + 1:])
        return halves_arr

    def add(self, arr):
        arr.sort()
        halves_arr = self.halve_arr(arr)
        for i in range(len(self.tree)):
            if len(halves_arr[i]) // 2:
                self.tree[i] = halves_arr[i][len(halves_arr[i]) // 2]
            else:
                self.tree[i] = halves_arr[i][0]


"""2 способ, такой же как и первый. только без создания экземпляра"""


def halve_arr(arr):
    halves_arr = [arr]

    for half in halves_arr:
        if half[:len(half) // 2]:
            halves_arr.append(half[:len(half) // 2])
            halves_arr.append(half[len(half) // 2 + 1:])
    return halves_arr


def create_node(key, level):
    return {'key': key, 'level': level}


def arr_to_bst(h, arr):
    tree = [None] * (pow(2, h + 1) - 1)
    arr.sort()
    halves_arr = halve_arr(arr)

    for i in range(len(tree)):

        if len(halves_arr[i]) // 2:
            tree[i] = create_node(halves_arr[i][len(halves_arr[i]) // 2], None)
        else:
            tree[i] = create_node(halves_arr[i][0], None)

        if i == 0:
            tree[i]['level'] = 1
        else:
            tree[i]['level'] = tree[(i - 1) // 2]['level'] + 1

    return tree


"""3 способ с классом Node"""


class Node:
    def __init__(self, k):
        self.left_child = None
        self.right_child = None
        self.key = k
        self.level = None


def arr_to_bst2(arr):
    if not arr:
        return None
    mid = len(arr)//2
    root = Node(arr[mid])
    root.left_child = arr_to_bst2(arr[:mid])
    root.right_child = arr_to_bst2(arr[mid+1:])
    return root


def preoder(root):
    yield root
    if root.left_child:
        yield from preoder(root.left_child)
    if root.right_child:
        yield from preoder(root.right_child)
