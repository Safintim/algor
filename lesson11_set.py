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


h = PowerSet(17, 3)
test_list = [3, 93, 60, 25, 73, 83, 45, 29, 18, 8, 28, 48, 40, 88, 0, 32, 15]
h2 = PowerSet(10, 3)


for i in test_list:
    h.put(i)
for i in range(93, 103):
    h2.put(i)
print(h.slots)
print(h2.slots)
# intersection
h3 = h.intersection(h2)
print(h3.slots)

# union
h3 = h.union(h2)
print(h3.slots)

# difference
h3 = h.difference(h2)
print(h3.slots)

test_issubset1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_issubset2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
h = PowerSet(sz=len(test_issubset1))
h2 = PowerSet(sz=len(test_issubset2))
# issubset
for i in test_issubset1:
    h.put(i)
for i in test_issubset2:
    h2.put(i)
print(h.issubset(h2))
