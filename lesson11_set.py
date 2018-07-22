#!/usr/bin/python3
"""Множества. код основан на lesson9_hash.py"""

from lesson9_hash import HashTable


class PowerSet(HashTable):

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
        else:
            print('элемента во множестве нет')
            return None

    def intersection(self, powset):
        a = self
        b = powset
        if len(a.slots) > len(b.slots):
            a, b = b, a
        c = PowerSet(sz=len(a.slots))
        for item in a.slots:
            if b.find(item) is not None:
                c.put(item)

        return c

    def union(self, powset):
        length = len(self.slots) + len(self.slots)
        c = PowerSet(sz=length)
        for item in self.slots:
            c.put(item)
        for item in powset.slots:
            c.put(item)
        return c

    def difference(self, powset):
        c = PowerSet(sz=len(self.slots))
        for item in self.slots:
            if powset.find(item) is None:
                c.put(item)
        return c

    def issubset(self, powset):
        for item in self.slots:
            if powset.find(item) is None:
                return False
        return True
