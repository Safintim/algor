import ctypes
"""
Динамический массив
"""


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

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

    def append(self, item):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)

        self.array[self.count] = item
        self.count += 1

    def insert(self, i, item):
        try:
            self.__getitem__(i)
            new_array = []
            if self.count == self.capacity:
                self.resize(2 * self.capacity)

            for k in range(i + 1):
                new_array.append(self.array[k])

            new_array[i] = item

            for k in range(i, self.count):
                new_array.append(self.array[k])

            self.array = new_array
            self.count += 1
        except (ValueError, IndexError):
            print('Index is out of bounds')

    def delete(self, i):
        try:
            self.__getitem__(i)
            if self.count <= int(self.capacity // 2):
                if self.capacity // 1.5 > 16:
                    self.resize(int(self.capacity // 1.5))
                else:
                    self.capacity = 16

            for k in range(i, self.count - 1):
                self.array[k] = self.array[k + 1]
            self.count -= 1

        except IndexError:
            print('Index is out of bounds')

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
