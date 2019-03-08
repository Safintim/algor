from random import choice


class HashTable:

    def __init__(self, sz=170):
        self.size = sz
        self.slots = [None] * self.size
        self.hash_f = choice([
            lambda x: ((16 * x + 51) % 293) % self.size,
            lambda x: ((7 * x + 93) % 313) % self.size,
            lambda x: ((311 * x + 18) % 307) % self.size,
            lambda x: ((347 * x - 84) % 311) % self.size,
        ])

    def hash_fun(self, value):
        return self.hash_f(value)

    def put(self, value):
        index = self.hash_fun(value)
        if self.slots[index] is None:
            self.slots[index] = [value]
        else:
            self.slots[index].append(value)
