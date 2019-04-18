def halves(result, a, i):
    if not a:
        return None
    result[i] = a[len(a) // 2]
    halves(result, a[:len(a) // 2], 2 * i+1)
    halves(result, a[len(a) // 2 + 1:], 2 * i+2)


def GenerateBBSTArray(a):
    a.sort()
    result = [None] * len(a)
    halves(result, a, 0)
    return result


class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BalancedBST:

    def __init__(self):
        self.Root = None
        self.BSTArray = []

    def create_nodes_from_list(self, bstarray):
        for i, key in enumerate(bstarray):
            if i == 0:
                new_node = BSTNode(bstarray[0], None)
                self.Root = new_node
            else:
                new_node = BSTNode(bstarray[i], bstarray[(i - 1) // 2])
            bstarray[i] = new_node

    def add_child_and_set_level(self, bstarray):
        for i, node in enumerate(bstarray):
            if i * 2 + 1 < len(bstarray):
                node.LeftChild = bstarray[i * 2 + 1]
                node.RightChild = bstarray[i * 2 + 2]
                if i == 0:
                    node.Level = 1
                    continue
                node.Level = bstarray[(i - 1) // 2].Level + 1
                i += 1
            else:
                node.Level = bstarray[(i - 1) // 2].Level + 1

    def CreateFromArray(self, a):
        self.BSTArray = GenerateBBSTArray(a)

    def GenerateTree(self):
        bstarray = self.BSTArray[:]

        self.create_nodes_from_list(bstarray)
        self.add_child_and_set_level(bstarray)

    def in_order(self, root_node):
        if root_node.LeftChild:
            yield from self.in_order(root_node.LeftChild)
        yield root_node
        if root_node.RightChild:
            yield from self.in_order(root_node.RightChild)

    def WideAllNodes(self, root_node):
        result = []
        queue = [root_node]
        while len(queue) > 0:
            node = queue.pop()
            result.append(node)

            if node.LeftChild is not None:
                queue.insert(0, node.LeftChild)
            if node.RightChild is not None:
                queue.insert(0, node.RightChild)

        return tuple(result)

    def is_keys_correct_order(self, root_node):
        for node in self.WideAllNodes(root_node):
            if node.LeftChild:
                if node.LeftChild.NodeKey > node.NodeKey:
                    return False

            if node.RightChild:
                if node.RightChild.NodeKey < node.NodeKey:
                    return False
        return True

    def is_equality_length(self, root_node):
        if root_node.LeftChild:
            max_left_level = max(i.Level for i in self.in_order(root_node.LeftChild))
        else:
            max_left_level = 1

        if root_node.RightChild:
            max_right_level = max(i.Level for i in self.in_order(root_node.RightChild))
        else:
            max_right_level = 1


        return abs(max_left_level - max_right_level) <= 1

    def IsBalanced(self, root_node):
        return self.is_keys_correct_order(root_node) and self.is_equality_length(root_node)
