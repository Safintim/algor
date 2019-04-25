# from lesson5_stack import Stack
# from lesson6_queue import Queue

#
#
#
#     def print_path(self, end):
#         # если использовать массив предков
#         # temp = ''
#         # for i in range(len(p)):
#         #     if end == start:
#         #         temp += self.vertex[end].name
#         #         return temp[::-1]
#         #     temp += self.vertex[end].name + '-'
#         #     end = p[end]
#         if end.parent is None:
#             return end.name
#         else:
#             return self.print_path(end.parent) + end.name
#
#     def bfs(self, current, end_path):
#         # 0 - исходное состояние
#         queue = Queue()
#         for v in self.vertex:
#             v.hit = False
#             v.parent = None
#
#         # parents = [0] * self.max_vertex  # массив предков. p[i] = c_i -> c_i предок i
#         start_i = self.vertex.index(current)  # индекс начало пути
#         ep_i = self.vertex.index(end_path)  # индекс конца пути
#
#         # parents[start_i] = start_i
#         flag = False
#
#         # 1 - фиксируем текущую как посещенную
#         current.hit = True
#
#         while True:
#             c_i = self.vertex.index(current)  # индекс текущей вершины
#
#             # 2 - из всех смежных вершин выбираем любую непосещенную
#             for i, value in enumerate(self.m_adjacency[c_i]):
#                 if value == 1 and not self.vertex[i].hit:
#                     self.vertex[i].parent = self.vertex[c_i]
#                     # parents[i] = c_i  # добавляем предка
#                     flag = False
#                     self.vertex[i].hit = True
#                     queue.enqueue(self.vertex[i])
#                     break
#                 elif value == 1:
#                     flag = True
#
#             # 2 - если нет непосещенных вершин
#             if flag:
#                 # если массив пуст, то значит изучили весь граф и пора печатать путь
#                 if queue.size() == 0:
#                     # return self.print_path(parents, start_i, ep_i)
#                     return self.print_path(end_path)
#                 else:
#                     current = queue.dequeue()
#
#
# class Vertex:
#
#     def __init__(self, name=None):
#         self.name = name
#         self.hit = False
#         self.parent = None
#


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
        while True:

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

            VFrom = self.vertex.index(current)
            if self.m_adjacency[VFrom][VTo] == 1:
                stack.push(self.vertex[VTo])
                break
            else:
                current = self.find_adjacent_vertex(VFrom)

        return stack.stack[::-1]
