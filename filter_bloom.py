from bitarray import bitarray


class BloomFilter:

    def __init__(self, f_len=32):
        self.filter_len = f_len
        self.filter = bitarray(f_len)
        self.filter.setall(0)

    def hash1(self, str1):
        # 17
        code = 0
        for c in str1:
            code = (code * 17 + ord(c))
        return code % self.filter_len

    def hash2(self, str1):
        # 223
        code = 0
        for c in str1:
            code = code * 223 + ord(c)
        return code % self.filter_len

    def add(self, str1):
        # добавляем строку str1 в фильтр
        self.filter[self.hash1(str1)] = 1
        self.filter[self.hash2(str1)] = 1

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        if self.filter[self.hash1(str1)] == 1 and self.filter[self.hash2(str1)] == 1:
            return True

        return False

