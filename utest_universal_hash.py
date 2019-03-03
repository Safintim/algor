import unittest
import universal_hash as l


class HashTest(unittest.TestCase):

    def test_put(self):
        test_list = [3, 93, 60, 25, 73, 83, 45, 29, 18, 8, 28, 48, 40, 88, 0, 32, 15]
        h1 = l.HashTable(17, 3)
        h2 = l.HashTable(17, 3)
        h3 = l.HashTable(17, 3)

        for i in test_list:
            h1.put(i)
            h2.put(i)
            h3.put(i)

        print(h1.slots)
        print(h2.slots)
        print(h3.slots)


if __name__ == '__main__':
    unittest.main()
