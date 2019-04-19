class Heap:

    def __init__(self):
        self.HeapArray = []
        self.HeapSize = 0

    def max_child(self, left, right):
        if self.HeapArray[left] - self.HeapArray[right] > 0:
            return left
        else:
            return right

    def shift_down(self):
        self.HeapArray.insert(0, self.HeapArray.pop(len(self.HeapArray)-1))
        shifted_element = self.HeapArray[0]
        i = 0
        while i * 2 + 1 < len(self.HeapArray) - 1:
            max_ch = self.max_child(i * 2 + 1, i * 2 + 2)

            if shifted_element < self.HeapArray[max_ch]:
                self.HeapArray[i], self.HeapArray[max_ch] = self.HeapArray[max_ch], self.HeapArray[i]

            i = max_ch

    def shift_up(self):
        shifted_element = self.HeapArray[-1]
        i = len(self.HeapArray) - 1

        while i > 0:
            if shifted_element > self.HeapArray[(i - 1) // 2]:
                self.HeapArray[i], self.HeapArray[(i - 1) // 2] = self.HeapArray[(i - 1) // 2], self.HeapArray[i]

            i = (i - 1) // 2

    def MakeHeap(self, a):
        self.HeapSize = len(a)
        for key in a:
            self.Add(key)

    def GetMax(self):
        if self.HeapArray:
            max_element = self.HeapArray.pop(0)
            if len(self.HeapArray):
                self.shift_down()
            return max_element
        return -1

    def Add(self, key):
        if len(self.HeapArray) < self.HeapSize:
            self.HeapArray.append(key)
            self.shift_up()
            return True
        return False
