import random
import unittest
import universal_hash as l


class HashTest(unittest.TestCase):

    def random_list_int(self, size):
        ints = set()
        while len(ints) != size:
            ints.add(random.randint(0, 1000))

        return list(ints)

    def count_none(self, l):
        count = 0
        for elem in l:
            if elem is None:
                count += 1

        return count

    def test_random_list_int(self):
        print(self.random_list_int(10))

    def test_put(self):
        test_list = [3, 93, 60, 25, 73, 83, 45, 29, 18, 8, 28, 48, 40, 88, 0, 32, 15]
        test_list = self.random_list_int(170)
        h1 = l.HashTable(170)
        h2 = l.HashTable(170)
        h3 = l.HashTable(170)

        for i in test_list:
            h1.put(i)
            h2.put(i)
            h3.put(i)

        print(h1.slots)
        print(h2.slots)
        print(h3.slots)

        print(self.count_none(h1.slots))
        print(self.count_none(h2.slots))
        print(self.count_none(h3.slots))


if __name__ == '__main__':
    unittest.main()
