class aBST:

    def __init__(self, depth):
        tree_size = 2**(depth+1) - 1
        self.Tree = [None] * tree_size

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

        return None

    def AddKey(self, key):
        index = self.FindKeyIndex(key)

        if index is None:
            return -1
        if index <= 0:
            self.Tree[abs(index)] = key
        return abs(index)


def halves(result, a, i):
    if not a:
        return None

    result[i] = a[len(a) // 2]
    halves(result, a[:len(a) // 2], 2*i+1)
    halves(result, a[len(a) // 2 + 1:], 2*i+2)


def GenerateBBSTArray(a):
    a.sort()
    result = [None] * len(a)
    halves(result, a, 0)
    return result
