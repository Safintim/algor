#!/usr/bin/python3
"""Множества. код основан на lesson9_hash.py"""

from lesson9_hash import HashTable


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
        return self.sizez

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
