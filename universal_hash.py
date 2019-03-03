from random import choice


class HashTable:

    def __init__(self, sz=17, stp=3):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.hash_f = choice([
            lambda x: ((1 * x + 0) % 80) % self.size,
            lambda x: ((1 * x + 0) % 60) % self.size,
            lambda x: ((1 * x + 0) % 70) % self.size
        ])

    def hash_fun(self, value):
        return self.hash_f(value)

    def put(self, value):
        index = self.hash_fun(value)
        if self.slots[index] is None:
            self.slots[index] = [value]
        else:
            self.slots[index].append(value)
