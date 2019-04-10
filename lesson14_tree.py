class SimpleTreeNode:

    def __init__(self, parent, value=None):
        self.Parent = parent
        self.Children = []
        self.NodeValue = value
        self.level = -1


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    @staticmethod
    def AddChild(parent, node):
        parent.Children.append(node)
        node.parent = parent
        # node.level = parent.level + 1

    def DeleteNode(self, node):
        if node != self.Root:
            parent = node.Parent
            for index, n in enumerate(parent.Children, 0):
                if n == node:
                    parent.Children.pop(index)

    def GetAllNodes(self, node):
        yield node
        for ch in node.Children:
            yield from self.GetAllNodes(ch)

    def __iter__(self):
        return self

    def FindNodesByValue(self, value):
        result = []
        for node in self.GetAllNodes(self.Root):
            if node.NodeValue == value:
                result.append(node)
        return result

    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode != self.Root:
            self.DeleteNode(OriginalNode)
            self.AddChild(NewParent, OriginalNode)

    def Count(self):
        count_node = 0
        for node in self.GetAllNodes(self.Root):
            if node.Children:
                count_node += 1
        return count_node

    def LeafCount(self):
        count_leaf = 0
        for node in self.GetAllNodes(self.Root):
            if not node.Children:
                count_leaf += 1

        return count_leaf

    def set_level(self):
        for n in self.GetAllNodes(self.Root):
            if n == self.Root:
                n.level = 1
            else:
                n.level = n.Parent.level + 1
        return
