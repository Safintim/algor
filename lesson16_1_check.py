def halves(result, a, i):
    if not a:
        return None

    current_node = BSTNode(a[len(a) // 2], result[(i - 1) // 2])
    if i != 0:
        current_node.Level = result[(i - 1) // 2].Level + 1
    result[i] = current_node
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
        self.Level = 1


class BalancedBST:

    def __init__(self):
        self.Root = None
        self.BSTArray = []

    def CreateFromArray(self, a):
        self.BSTArray = GenerateBBSTArray(a)

    def GenerateTree(self):
        i = 0
        self.Root = self.BSTArray[0]
        while i * 2 + 1 < len(self.BSTArray):

            self.BSTArray[i].LeftChild = self.BSTArray[i * 2 + 1]
            self.BSTArray[i].RightChild = self.BSTArray[i * 2 + 2]

            i += 1
