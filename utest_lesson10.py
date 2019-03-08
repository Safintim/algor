import unittest
import lesson10_ass_arr as l


class DictTest(unittest.TestCase):

    @staticmethod
    def create_dict():
        test_list = [3, 93, 60, 25, 73, 83, 45, 29, 18, 8, 28, 48, 40, 88, 0, 32, 15]
        h = l.NativeDictionary(17)

        for i in range(97, 114):
            h[chr(i)] = test_list[i - 97]

        return h

    def test_put(self):
        h = self.create_dict()
        for i in h.slots:
            h[i] = 0
        self.assertEqual(h.put('zx', 100), None)
        self.assertEqual(h.values, [0] * len(h.values))

    def test_find(self):
        h = self.create_dict()
        index = h.find('a')
        key = h.slots[index]
        self.assertEqual(h.slots[index], 'a')
        self.assertEqual(h[key], 3)

    def test_get(self):
        h = self.create_dict()
        self.assertEqual(h.get('a'), 3)
        self.assertEqual(h.get('key'), None)

    def test_is_key(self):
        h = self.create_dict()
        self.assertTrue(h.is_key('f'))
        self.assertTrue(h.is_key('g'))
        self.assertFalse(h.is_key(100))
        self.assertFalse(h.is_key(28))
        self.assertFalse(h.is_key('u'))


if __name__ == '__main__':
    unittest.main()
