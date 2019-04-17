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

    def CreateFromArray(self, a):
        self.BSTArray = GenerateBBSTArray(a)

    def GenerateTree(self):
        bstarray = self.BSTArray[:]

        for i, key in enumerate(bstarray):
            if i == 0:
                new_node = BSTNode(self.BSTArray[0], None)
                self.Root = new_node
            else:
                new_node = BSTNode(bstarray[i], bstarray[(i - 1) // 2])
            bstarray[i] = new_node

        i = 0
        while i * 2 + 1 < len(bstarray):
            node = bstarray[i]
            node.LeftChild = bstarray[i * 2 + 1]
            node.RightChild = bstarray[i * 2 + 2]
            if i != 0:
                node.Level = bstarray[(i - 1) // 2].Level + 1
            else:
                node.Level = 1
            i += 1
