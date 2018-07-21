from random import randint
"""
Ассоциативный массив. код основан на lesson9_hash.py
"""


class HashTable:

    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, value):
        summ = 0
        i = 1
        for ch in str(value):
            summ += ord(ch) * i
            i += 1
        return summ % self.size

    def rotate(self, k, step):
        return (k + self.step) % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        temp = 0

        if self.slots[index] is None:
            return index
        else:
            while temp < 2 * (self.size // self.step):
                for k in range(index, self.size, self.step):
                    if self.slots[k] is None:
                        return k
                temp += 1
                index = self.rotate(k, self.step)
            else:
                if None not in self.slots:
                    return None

    def put(self, key, value):
        index = self.hash_fun(key)
        if self.slots[index] == key:
            self.values[index] = value
            return True

        index = self.seek_slot(key)
        if index is not None:
            self.slots[index] = key
            self.values[index] = value
            return True
        else:
            print('Нет мест, размер таблицы: {}'.format(self.size))
            return None

    def get(self, key):
        key = self.find(key)
        if key is None:
            return None
        else:
            return self.values[key]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)

    def is_key(self, key):
        if self.find(key) is None:
            return None
        else:
            return True

    def find(self, value):
        index = self.hash_fun(value)
        temp = 0
        if self.slots[index] == value:
            return index
        else:
            while temp < 2 * (self.size // self.step):
                for k in range(index, self.size, self.step):
                    if self.slots[k] == value:
                        return k
                temp += 1
                index = self.rotate(k, 2)

        return None
