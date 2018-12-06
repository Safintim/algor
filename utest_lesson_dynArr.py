import unittest
import lesson4_dynArr as l


class DaTest(unittest.TestCase):

    def test_insert(self):
        array = l.DynArray()
        array.insert(0, 100)
        self.assertEqual(array[0], 100)
        self.assertEqual(array.count, 1)
        self.assertEqual(array.capacity, 16)
        print(array.convert_to_arr())

        array = l.create_da(10)
        self.assertEqual(array.count, 10)
        self.assertEqual(array.capacity, 16)
        array.insert(4, 100)
        self.assertEqual(array.count, 11)
        self.assertEqual(array.capacity, 16)
        self.assertEqual(array[4], 100)
        print(array.convert_to_arr())

        array = l.create_da(16)
        array.insert(16, 100)
        self.assertEqual(array.count, 17)
        self.assertEqual(array.capacity, 32)
        self.assertEqual(array[array.count-1], 100)
        print(array.convert_to_arr())

        array = l.create_da(17)
        with self.assertRaises(IndexError):
            array.insert(-1, 100)
        with self.assertRaises(IndexError):
            array.insert(18, 100)
        self.assertEqual(array.count, 17)
        self.assertEqual(array.capacity, 32)
        print(array.convert_to_arr())

    def test_delete(self):
        array = l.create_da(14)
        array.delete(0)
        self.assertEqual(array.count, 13)
        self.assertEqual(array.capacity, 16)
        self.assertEqual(array[0], 1)
        print(array.convert_to_arr())

        array = l.create_da(32)
        for i in range(17):
            array.delete(0)
        self.assertEqual(array.count, 15)
        self.assertEqual(array.capacity, 21)
        print(array.convert_to_arr())

        array = l.create_da(32)
        with self.assertRaises(IndexError):
            array.delete(-1)
        with self.assertRaises(IndexError):
            array.delete(32)
        self.assertEqual(array.count, 32)
        self.assertEqual(array.capacity, 32)
        print(array.convert_to_arr())


if __name__ == '__main__':
    unittest.main()
