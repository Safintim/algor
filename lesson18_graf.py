class SimpleGraph:

    def __init__(self, mv):
        self.max_vertex = mv
        self.m_adjacency = [[0] * mv for _ in range(mv)]
        self.vertex = []

    def add_vertex(self, v):
        self.vertex.append(v)
        if len(self.vertex) > self.max_vertex:
            [i.append(0) for i in self.m_adjacency]
            self.max_vertex += 1
            self.m_adjacency.append([0] * self.max_vertex)

    def add_edge(self, v1, v2):
        if v1 in self.vertex and v2 in self.vertex:
            v1_i = self.vertex.index(v1)
            v2_i = self.vertex.index(v2)
            self.m_adjacency[v1_i][v2_i] = 1
            self.m_adjacency[v2_i][v1_i] = 1
        else:
            print('Какой-то вершины нет')

    def remove_edge(self, v1, v2):
        if v1 in self.vertex and v2 in self.vertex:
            v1_i = self.vertex.index(v1)
            v2_i = self.vertex.index(v2)
            self.m_adjacency[v1_i][v2_i] = 0
            self.m_adjacency[v2_i][v1_i] = 0
        else:
            print('Какой-то вершины нет')

    def remove_vertex(self, v):
        if v in self.vertex:
            v_i = self.vertex.index(v)
            # удаляем столбец вершины
            for col in self.m_adjacency:
                col.pop(v_i)
            # удаляем строку вершины
            self.m_adjacency.pop(v_i)
            self.vertex.pop(v_i)
            self.max_vertex -= 1
        else:
            print('Такой вершины нет')


class Vertex:
    pass
