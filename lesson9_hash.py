""""Хэш-таблица"""
from random import randint

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

    def rotate(self, k):
        if k == self.size:
            return 0
        elif k < self.size:
            return self.step - (self.size - k)

    def seek_slot(self, value):
        index = self.hash_fun(value)
        temp = 0

        if self.slots[index] is None:
            return index
        elif None not in self.slots:
            return None
        else:

            while 1:
                for k in range(index, self.size, self.step):
                    temp = k
                    if self.slots[k] is None:
                        return k

                index = self.rotate(temp)
                # вместо этого можно по идее вычислять хэш повторно.
                # то есть предыдущий value изменять на какое-то значение и пересчитывать хэш
                # if k == self.size:
                #     index = 0
                # elif k < self.size:
                #     index = self.step - (self.size - k)

    def put(self, value):
        index = self.seek_slot(value)
        self.slots[index] = value

    # def find(self, value):
    #     index = self.hash_fun(value)
    #
    #     if self.slots[index] == value:
    #         return self.slots[index]
    #     else:


h = HashTable(17, 3)
test_list = [3, 93, 60, 25, 73, 83, 45, 29, 18, 8, 28, 48, 40, 88, 0, 32, 15]
result_list = [3, 48, 15, 25, 73, 83, 93, 40, 45, 18, 88, 29, 8, 0, 60, 28, 32]
hash_list = []
a = h.hash_fun(3)
b = h.hash_fun(a+3+3+3)
print(a, b)
# for i in test_list:
#     hash_list.append(h.hash_fun(i))
# for i in test_list:
#     h.put(i)
#
# #
# print(h.slots == result_list)
# print(h.slots)
# print(result_list)
# print(test_list)
# h.put(2)
# for i in range(17):
#     print(h.slots[i], hash_list[i], test_list[i])


