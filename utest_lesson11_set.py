import unittest
import lesson11_set as l


class SetTest(unittest.TestCase):

    @staticmethod
    def create_set():
        h = l.PowerSet(17)
        h2 = l.PowerSet(5)
        test_list = [3, 93, 60, 25, 73, 83, 45, 29, 18, 8, 28, 48, 40, 88, 0, 32, 15]

        for i in test_list:
            h.put(i)
        for i in range(93, 98):
            h2.put(i)
        return h, h2

    def test_put(self):
        h = l.PowerSet(5, 3)
        result = [320, None, None, 120, 220]
        h.put(120)
        h.put(220)
        h.put(320)

        h.put(120)
        h.put(220)
        h.put(320)
        self.assertTrue(h.slots == result)

    def test_remove(self):
        h = l.PowerSet(5, 3)
        for i in range(120, 620, 100):
            h.put(i)
        h.remove(520)
        h.remove(120)
        self.assertEqual(h.find(520), None)
        self.assertEqual(h.find(120), None)

    def test_intersection(self):
        result = [93]
        temp = self.create_set()
        h1 = temp[0]
        h2 = temp[1]
        h1.intersection(h2)
        self.assertEqual(h1.slots, h1.size(), result)

    def test_union(self):
        temp = self.create_set()
        h1 = temp[0]
        h2 = temp[1]
        # h2.slots = []
        print(h1.slots)
        h1.union(h2)
        print(h1.slots, h1.size, len(h1.slots))

    def test_difference(self):
        temp = self.create_set()
        h1 = temp[0]
        h2 = temp[1]
        h1.difference(h2)

        self.assertEqual(h1.find(93), None)

    def test_issubset(self):
        test_issubset1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_issubset2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        h = l.PowerSet(sz=len(test_issubset1))
        h2 = l.PowerSet(sz=len(test_issubset2))
        for i in test_issubset1:
            h.put(i)
        for i in test_issubset2:
            h2.put(i)

        r1 = h.issubset(h2)
        r2 = h2.issubset(h)

        self.assertTrue(r1)
        self.assertFalse(r2)


if __name__ == '__main__':
    unittest.main()
