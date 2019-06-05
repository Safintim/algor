class SimpleTreeNode:

    def __init__(self, value, parent):
        self.Parent = parent
        self.Children = []
        self.NodeValue = value
        self.level = -1


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        # node.level = parent.level + 1

    def traverse(self, node):
        yield node
        for ch in node.Children:
            yield from self.traverse(ch)

    def GetAllNodes(self):
        return [i for i in self.traverse(self.Root)]

    def DeleteNode(self, nodetodelete):
        if nodetodelete != self.Root and nodetodelete in self.GetAllNodes():
            nodetodelete.Parent.Children.remove(nodetodelete)

    def FindNodesByValue(self, value):
        return [node for node in self.GetAllNodes() if node.NodeValue == value]

    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode != self.Root:
            self.DeleteNode(OriginalNode)
            self.AddChild(NewParent, OriginalNode)

    def Count(self):
        return len([i for i in self.GetAllNodes()])

    def LeafCount(self):
        count_leaf = 0
        for node in self.GetAllNodes():
            if not node.Children:
                count_leaf += 1
        return count_leaf

    def set_level(self):
        for n in self.GetAllNodes():
            if n == self.Root:
                n.level = 1
            else:
                n.level = n.Parent.level + 1
        return

    def EvenTrees(self):
        broken_edges = []

        number_broken_edges = 0
        number_odd = 0
        for child in self.Root.Children:
            number_children = len([node for node in self.traverse(child)])
            if (number_children != 0
                    and number_children % 2 == 0
                    and number_broken_edges < len(self.Root.Children) - 1):

                number_broken_edges += 1
                broken_edges.append(self.Root)
                broken_edges.append(child)
            elif number_children % 2 == 1:
                number_odd += number_children

        number_odd += 1  # прибавить корневой узел

        if len(broken_edges) > 0 and number_odd % 2 == 0:
            return broken_edges
        return []

