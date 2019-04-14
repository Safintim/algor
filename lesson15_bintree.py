class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:
    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def pre_order(self, node):
        yield node
        if node.LeftChild:
            yield from self.pre_order(node.LeftChild)
        if node.RightChild:
            yield from self.pre_order(node.RightChild)

    def in_order(self, node):
        if node.LeftChild:
            yield from self.in_order(node.LeftChild)
        yield node
        if node.RightChild:
            yield from self.in_order(node.RightChild)

    def post_order(self, node):
        if node.LeftChild:
            yield from self.post_order(node.LeftChild)
        if node.RightChild:
            yield from self.post_order(node.RightChild)
        yield node

    def DeepAllNodes(self, mode):
        if mode == 0:
            return tuple(self.in_order(self.Root))
        elif mode == 1:
            return tuple(self.pre_order(self.Root))
        else:
            return tuple(self.post_order(self.Root))

    def WideAllNodes(self):
        result = []
        queue = [self.Root]
        while len(queue) > 0:
            x = queue.pop()
            result.append(x)

            if x.LeftChild is not None:
                queue.insert(0, x.LeftChild)
            if x.RightChild is not None:
                queue.insert(0, x.RightChild)

        return tuple(result)

    def FindNodeByKey(self, key):
        current_node = self.Root
        bst_find = BSTFind()
        while current_node:
            if key == current_node.NodeKey:
                bst_find.Node = current_node
                bst_find.NodeHasKey = True
                break
            elif key < current_node.NodeKey:
                if current_node.LeftChild is None:
                    bst_find.Node = current_node
                    bst_find.ToLeft = True
                current_node = current_node.LeftChild
            else:
                if current_node.RightChild is None:
                    bst_find.Node = current_node
                current_node = current_node.RightChild

        return bst_find

    def AddKeyValue(self, key, val):
        bst_find = self.FindNodeByKey(key)

        if not bst_find.NodeHasKey:
            if bst_find.ToLeft:
                bst_find.Node.LeftChild = BSTNode(key, val, bst_find.Node)
            else:
                bst_find.Node.RightChild = BSTNode(key, val, bst_find.Node)
            return True
        return False

    def go_right(self, FromNode):
        while FromNode.RightChild:
            FromNode = FromNode.RightChild

        return FromNode

    def go_left(self, FromNode):
        while FromNode.LeftChild:
            FromNode = FromNode.LeftChild

        return FromNode

    def FinMinMax(self, FromNode, FindMax):
        if FindMax:
            desired_node = self.go_right(FromNode)
        else:
            desired_node = self.go_left(FromNode)
        return desired_node

    def change_parent(self, node, new_node):
        if node.Parent.LeftChild == node:
            node.Parent.LeftChild = new_node
        else:
            node.Parent.RightChild = new_node

    def DeleteNodeByKey(self, key):
        bst_find = self.FindNodeByKey(key)
        if bst_find.NodeHasKey:
            delete_node = bst_find.Node

            if delete_node.RightChild is None:
                self.change_parent(delete_node, None)
                return True

            desired_node = self.go_left(delete_node.RightChild)

            desired_node.Parent.LeftChild = None
            desired_node.Parent = delete_node.Parent
            self.change_parent(delete_node, desired_node)
            desired_node.LeftChild = delete_node.LeftChild

            if delete_node.RightChild != desired_node:
                desired_node.RightChild = delete_node.RightChild

            return True
        return False

    def GetAllNodes(self):
        return [i for i in self.pre_order(self.Root)]

    def Count(self):
        return len(self.GetAllNodes())
