class Heap:

    def __init__(self):
        self.heap = []

    def _shift_up(self, i):
        # i + 1 - чтобы первые два числа тоже сравнивались
        while (i+1) // 2 > 0:
            if self.heap[i] > self.heap[(i-1) // 2]:
                self.heap[i], self.heap[(i-1) // 2] = self.heap[(i-1) // 2], self.heap[i]
            i = (i - 1) // 2

    def add(self, node):
        self.heap.append(node)
        self._shift_up(len(self.heap)-1)

    def __max(self, child1, child2):
        if child1 == len(self.heap) - 1:
            return child1
        else:
            if self.heap[child1] > self.heap[child2]:
                return child1
            else:
                return child2

    def _shift_down(self):
        i = 0

        while (i * 2 + 2) <= len(self.heap):
            mx = self.__max(child1=i*2+1, child2=i*2+2)
            if self.heap[i] < self.heap[mx]:
                self.heap[i], self.heap[mx] = self.heap[mx], self.heap[i]
            i = mx

    def remove_max(self):
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self._shift_down()

    def max(self):
        return self.heap[0]

    def __iter__(self):
        return iter(self.heap)
