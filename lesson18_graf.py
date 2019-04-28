from itertools import combinations

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        if self.size() > 0:
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)


class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.size() > 0:
            return self.stack.pop(0)
        return None

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.size() > 0:
            return self.stack[0]
        return None

    def size(self):
        return len(self.stack)


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
        self.Parent = None


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * self.max_vertex for _ in range(self.max_vertex)]
        self.vertex = []

    def isVertex(self, v):
        if 0 <= v <= self.max_vertex:
            return True
        return False

    def AddVertex(self, v):
        self.vertex.append(Vertex(v))
        if len(self.vertex) > self.max_vertex:
            [i.append(0) for i in self.m_adjacency]
            self.max_vertex += 1
            self.m_adjacency.append([0] * self.max_vertex)

    def RemoveVertex(self, v):
        if self.isVertex(v):
            [i.pop(v) for i in self.m_adjacency]
            self.m_adjacency.pop(v)
            self.vertex.pop(v)
            self.max_vertex -= 1
            return True
        return False

    def IsEdge(self, v1, v2):
        if self.isVertex(v1) and self.isVertex(v2):
            if self.m_adjacency[v1][v2] == 1:
                return True
        return False

    def AddEdge(self, v1, v2):
        if self.isVertex(v1) and self.isVertex(v2):
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
            return True
        return False

    def RemoveEdge(self, v1, v2):
        if self.isVertex(v1) and self.isVertex(v2):
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0
            return True
        return False

    def find_adjacent_vertex(self, v):
        for i, value in enumerate(self.m_adjacency[v]):
            if value == 1 and not self.vertex[i].Hit:
                return self.vertex[i]
        return False

    def DepthFirstSearch(self, VFrom, VTo):
        stack = Stack()
        for v in self.vertex:
            v.Hit = False

        current = self.vertex[VFrom]
        current.Hit = True
        stack.push(current)
        while True:

            VFrom = self.vertex.index(current)
            if self.m_adjacency[VFrom][VTo] == 1:
                stack.push(self.vertex[VTo])
                break
            else:
                current = self.find_adjacent_vertex(VFrom)

            if not current:
                stack.pop()
                if stack.size() == 0:
                    return stack.stack
                else:
                    current = stack.stack[0]
                    current.Hit = True
            else:
                current.Hit = True
                stack.push(current)

        return stack.stack[::-1]

    def get_path_bfs(self, vertex):
        yield vertex
        if vertex.Parent is None:
            return vertex
        yield from self.get_path_bfs(vertex.Parent)

    def BreadthFirstSearch(self, VFrom, VTo):
        queue = Queue()
        for v in self.vertex:
            v.Hit = False
            v.Parent = None

        current = self.vertex[VFrom]
        current.Hit = True
        queue.enqueue(current)
        while True:
            index_current = self.vertex.index(current)
            adjacent_vertex = self.find_adjacent_vertex(index_current)

            if not adjacent_vertex:
                if queue.size():
                    current = queue.dequeue()
                else:
                    break
            else:
                adjacent_vertex.Parent = self.vertex[index_current]
                adjacent_vertex.Hit = True
                queue.enqueue(adjacent_vertex)

        return [i for i in self.get_path_bfs(self.vertex[VTo])][::-1]

    def WeakVertices(self):
        not_in_vertexes = []
        for i, vertex in enumerate(self.m_adjacency):
            adjacent_vertexes = [i for i, v in enumerate(vertex) if v == 1]
            if len(adjacent_vertexes) < 2:
                not_in_vertexes.append(self.vertex[i])
                break

            combinations_adjacent_vertexes = list(combinations(adjacent_vertexes, 2))

            not_triangle = True
            for v1, v2 in combinations_adjacent_vertexes:
                if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
                    not_triangle = False
                    break

            if not_triangle:
                not_in_vertexes.append(self.vertex[i])

        return not_in_vertexes
