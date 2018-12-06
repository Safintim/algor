import ctypes
"""
Динамический массив
"""


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def is_need_increase_buf(self):
        return self.count == self.capacity

    def is_need_reduce_buf(self):
        return self.count <= int(self.capacity // 2)

    def is_empty(self):
        return self.count == 0

    def is_min_capacity(self):
        return self.capacity // 1.5 > 16

    def append(self, item):
        if self.is_need_increase_buf():
            self.resize(2 * self.capacity)

        self.array[self.count] = item
        self.count += 1

    def insert(self, i, item):

        if i < 0 or i > self.count:
            return False

        if self.is_empty():
            self.append(item)
            return True

        if self.is_need_increase_buf():
            self.resize(2 * self.capacity)

        self.array = self.array[:i] + [item] + self.array[i:self.count]
        self.count += 1

        return True

    def delete(self, i):

        if i < 0 or i > self.count:
            return False

        if self.is_need_reduce_buf():
            if self.is_min_capacity():
                self.resize(int(self.capacity // 1.5))
            else:
                self.capacity = 16

        for k in range(i, self.count - 1):
            self.array[k] = self.array[k + 1]
        self.count -= 1

    def convert_to_arr(self):
        arr = []

        for i in range(self.count):
            arr.append(self.array[i])

        return arr


def create_da(n):
    da = DynArray()
    for i in range(n):
        da.append(i)
    return da
