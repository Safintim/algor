class Node:

    def __init__(self, parent):
        self.parent = parent
        self.left_child = None
        self.right_child = None

        self.color_parent = None
        self.color_right = None
        self.color_left = None

class Tree:
    def __init__(self, depth, colors):
        self.tree = [None] * (pow(2, depth) - 1)
        self.colors = [i for i in range(colors)]