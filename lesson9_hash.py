#!/usr/bin/python3
""""Хэш-таблица"""


class HashTable:

    def __init__(self, sz=17, stp=3):
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
        return (k + self.step) % self.size
        # ниже костыль
        # if k == self.size:
        #     return 0
        # elif k < self.size:
        #     return step - (self.size - k)

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
                # когда уже несколько раз прошлись по слотам
                # и не нашли место
                if None not in self.slots:
                    return None

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value

        return index

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
