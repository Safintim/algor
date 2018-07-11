""""Хэш-таблица"""


class HashTable:

    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        summ = 0
        i = 1
        for ch in str(value):
            summ += ord(ch) * i
            i += 1
        return summ % self.size

    def rotate(self, k, step):
        if k == self.size:
            return 0
        elif k < self.size:
            return step - (self.size - k)

    def seek_slot(self, value):
        index = self.hash_fun(value)

        if self.slots[index] is None:
            return index
        elif None not in self.slots:
            return None
        else:
            while True:
                for k in range(index, self.size, self.step):
                    if self.slots[k] is None:
                        return k
                index = self.rotate(k, self.step)

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
        else:
            print('Нет мест, размер таблицы: {}'.format(self.size))
            return None

    def find(self, value):
        old_index = self.hash_fun(value)
        stop = False

        if self.slots[old_index] == value:
            return self.slots[old_index]
        else:
            new_index = old_index
            while old_index != new_index:
                for k in range(new_index, self.size, self.step):
                    if self.slots[k] == value:
                        return self.slots[new_index]
                new_index = self.rotate(k, 2)

        return None


h = HashTable(17, 3)
test_list = [3, 93, 60, 25, 73, 83, 45, 29, 18, 8, 28, 48, 40, 88, 0, 32, 15]
result_list = [3, 48, 15, 25, 73, 83, 93, 40, 45, 18, 88, 29, 8, 0, 60, 28, 32]
hash_list = []

for i in test_list:
    h.put(i)

print(h.slots == result_list)
print(h.slots)
h.put(100)
print(h.find(3))
