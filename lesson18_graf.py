# from lesson5_stack import Stack
# from lesson6_queue import Queue

#
#     def dfs(self, current, end_path):
#         # 0 - исходное состояние
#         stack = Stack()
#         for v in self.vertex:
#             v.hit = False
#
#         ep_i = self.vertex.index(end_path)  # индекс конечного пути
#         flag = False
#
#         while True:
#
#             # если непосещенных больше нет, то пропустить след операции
#             if not flag:
#                 # 2-3 - фиксируем как посещенную и добавл в стек
#                 current.hit = True
#                 stack.push(current)
#
#             c_i = self.vertex.index(current)  # индекс текущей вершины
#
#             # 4 - среди смежных ищем целевую вершину
#             if self.m_adjacency[c_i][ep_i] == 1:
#                 stack.push(end_path)
#                 return '->'.join(str(i.name) for i in stack.stack[::-1])
#
#             # если нет, то выбираем такую смежную, которая еще не была посещена
#             for i, value in enumerate(self.m_adjacency[c_i]):
#                 if value == 1 and not self.vertex[i].hit:
#                     current = self.vertex[i]
#                     flag = False
#                     break  # нужно перейти к 2-3
#                 elif value == 1:
#                     flag = True
#
#             # 5 - если непосещенных больше нет
#             if flag:
#                 stack.pop()  # удаляем верхний элемент стека
#                 if stack.size() == 0:
#                     print('Путь не найден')
#                     return None
#                 else:
#                     current = stack.stack[0]  # текущий становится верхний элемент стека
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


class Vertex:

    def __init__(self, val):
        self.Value = val


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
