from lesson5_stack import Stack
from lesson6_queue import Queue

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

    def dfs(self, current, end_path):
        # 0 - исходное состояние
        stack = Stack()
        for v in self.vertex:
            v.hit = False

        ep_i = self.vertex.index(end_path)  # индекс конечного пути
        flag = False

        while True:

            # если непосещенных больше нет, то пропустить след операции
            if not flag:
                # 2-3 - фиксируем как посещенную и добавл в стек
                current.hit = True
                stack.push(current)

            c_i = self.vertex.index(current)  # индекс текущей вершины

            # 4 - среди смежных ищем целевую вершину
            if self.m_adjacency[c_i][ep_i] == 1:
                stack.push(end_path)
                return '->'.join(str(i.name) for i in stack.stack[::-1])

            # если нет, то выбираем такую смежную, которая еще не была посещена
            for i, value in enumerate(self.m_adjacency[c_i]):
                if value == 1 and not self.vertex[i].hit:
                    current = self.vertex[i]
                    flag = False
                    break  # нужно перейти к 2-3
                elif value == 1:
                    flag = True

            # 5 - если непосещенных больше нет
            if flag:
                stack.pop()  # удаляем верхний элемент стека
                if stack.size() == 0:
                    print('Путь не найден')
                    return None
                else:
                    current = stack.stack[0]  # текущий становится верхний элемент стека

    def print_path(self, p, start, end):
        '''Функция идет с конца пути к началу. Потом реверс строки'''
        temp = ''
        for i in range(len(p)):
            if end == start:
                temp += self.vertex[end].name
                return temp[::-1]
            temp += self.vertex[end].name + '-'
            end = p[end]

    def bfs(self, current, end_path):
        # 0 - исходное состояние
        queue = Queue()
        for v in self.vertex:
            v.hit = False

        parents = [0] * self.max_vertex  # массив предков. p[i] = c_i -> c_i предок i
        start_i = self.vertex.index(current)  # индекс начало пути
        ep_i = self.vertex.index(end_path)  # индекс конца пути

        parents[start_i] = start_i
        flag = False

        # 1 - фиксируем текущую как посещенную
        current.hit = True

        while True:
            c_i = self.vertex.index(current)  # индекс текущей вершины

            # 2 - из всех смежных вершин выбираем любую непосещенную
            for i, value in enumerate(self.m_adjacency[c_i]):
                if value == 1 and not self.vertex[i].hit:
                    parents[i] = c_i  # добавляем предка
                    flag = False
                    self.vertex[i].hit = True
                    queue.enqueue(self.vertex[i])
                    break
                elif value == 1:
                    flag = True

            # 2 - если нет непосещенных вершин
            if flag:
                # если массив пуст, то значит изучили весь граф и пора печатать путь
                if queue.size() == 0:
                    return self.print_path(parents, start_i, ep_i)
                else:
                    current = queue.dequeue()


class Vertex:

    def __init__(self, name=None):
        self.name = name
        self.hit = False
