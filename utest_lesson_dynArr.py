import unittest
import lesson4_dynArr as l


class DaTest(unittest.TestCase):

    def test_insert(self):
        array = l.DynArray()
        array.insert(0, 100)
        self.assertEqual(array[0], 100)

        array = l.create_da(10)
        self.assertEqual(array.count, 10)
        self.assertEqual(array.capacity, 16)
        array.insert(4, 100)
        self.assertEqual(array.count, 11)
        self.assertEqual(array.capacity, 16)
        self.assertEqual(array[4], 100)

        array = l.create_da(16)
        array.insert(14, 100)
        self.assertEqual(array.count, 17)
        self.assertEqual(array.capacity, 32)

        array = l.create_da(17)
        array.insert(-1, 100)
        array.insert(18, 100)
        self.assertEqual(array.count, 17)
        self.assertEqual(array.capacity, 32)

    def test_delete(self):
        array = l.create_da(14)
        array.delete(0)
        self.assertEqual(array.count, 13)
        self.assertEqual(array.capacity, 16)
        self.assertEqual(array[0], 1)

        array = l.create_da(32)
        for i in range(17):
            array.delete(0)
        self.assertEqual(array.count, 15)
        self.assertEqual(array.capacity, 21)

        array = l.create_da(32)
        array.delete(-1)
        array.delete(33)
        self.assertEqual(array.count, 32)
        self.assertEqual(array.capacity, 32)


if __name__ == '__main__':
    unittest.main()
