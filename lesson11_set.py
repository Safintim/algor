#!/usr/bin/python3
"""Множества. код основан на lesson9_hash.py"""


class HashTable:

    def __init__(self, sz=17, stp=3):
        self.sizez = sz
        self.step = stp
        self.slots = [None] * self.sizez

    def hash_fun(self, value):
        summ = 0
        i = 1
        for ch in str(value):
            summ += ord(ch) * i
            i += 1
        return summ % self.sizez

    def rotate(self, k, step):
        return (k + self.step) % self.sizez
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
            while temp < 2 * (self.sizez // self.step):
                for k in range(index, self.sizez, self.step):
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
            while temp < 2 * (self.sizez // self.step):
                for k in range(index, self.sizez, self.step):
                    if self.slots[k] == value:
                        return k
                temp += 1
                index = self.rotate(k, 2)

        return None


class PowerSet(HashTable):

    def new_power_set(self, c, stp=3):
        self.__init__(len(c), stp=stp)
        for item in c:
            self.put(item)

    def put(self, value):
        index = self.find(value)
        if index is not None:
            # print(value, ' Такой элемент уже есть во множестве')
            return None

        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
        else:
            print('Нет мест, размер таблицы: {}'.format(self.size))
            return None

    def remove(self, value):
        index = self.find(value)
        if index is not None:
            self.slots[index] = None
            return True
        return False

    def get(self, key):
        key = self.find(key)
        if key is not None:
            return True

        return False

    def size(self):
        count = 0
        for i in self.slots:
            if i is not None:
                count += 1
        return count

    def intersection(self, powset):
        a = self
        b = powset
        c = []
        if len(a.slots) > len(b.slots):
            a, b = b, a

        for item in a.slots:
            if b.find(item) is not None:
                c.append(item)

        self.new_power_set(c)

        return None

    def union(self, powset):
        if powset.slots:
            c = []
            for item in self.slots:
                c.append(item)
            for item in powset.slots:
                if item not in self.slots:
                    c.append(item)
            self.new_power_set(c, stp=5)

        return None

    def difference(self, powset):
        c = []
        for item in self.slots:
            if powset.find(item) is None:
                c.append(item)
        self.new_power_set(c)
        return None

    def issubset(self, powset):
        for item in self.slots:
            if powset.find(item) is None:
                return False
        return True
