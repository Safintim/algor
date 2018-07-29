class Heap:

    def __init__(self):
        self.heap = []

    def _add(self, i):
        for current in range(i, 0, -1):
            parent = (current - 1) // 2
            if self.heap[current] == self.heap[parent]:
                return 'Такой уже есть'
            elif self.heap[current] < self.heap[parent]:
                return True
            else:
                # self.heap[current] > self.heap[index]
                self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
                return self._add(parent)

    def add(self, node):
        self.heap.append(node)
        result = self._add(len(self.heap)-1)
        return result

    def __max(self, current, child):
        if self.heap[current] > self.heap[child]:
            return True
        else:
            self.heap[current], self.heap[child] = self.heap[child], self.heap[current]
            return False

    def _remove_max(self, i=0):

        for current in range(i, len(self.heap)):

            child1 = 2 * current + 1
            child2 = 2 * current + 2

            if len(self.heap) - 1 < child1:
                # если нет ребенка
                pass
            elif len(self.heap) - 1 == child1:
                # если один ребенок
                self.__max(current, child1)
            else:
                # если есть два ребенка
                if self.heap[child1] > self.heap[child2]:
                    child = child1
                else:
                    child = child2
                if self.__max(current, child):
                    pass
                else:
                    return self._remove_max(child)

            return True

    def remove_max(self):
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self._remove_max()

    def max(self):
        return self.heap[0]

    def __iter__(self):
        return iter(self.heap)
