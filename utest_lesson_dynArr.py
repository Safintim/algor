import unittest
import lesson4_dynArr as Da


class DaTest(unittest.TestCase):

    def test_insert(self):
        result_arr = [300, 0, 1, 2, 3, 4, 200, 5, 6, 7, 8, 9, 10, 11, 12, 13, 400, 14]
        array = Da.create_da(15)

        array.insert(5, 200)
        array.insert(0, 300)
        array.insert(16, 400)
        print('Step 4. Check exception i={0}, item={1}:'.format(-16, 400), end=' ')
        array.insert(-16, 400)

        self.assertEqual(array.count, len(result_arr))
        self.assertEqual(array.capacity, 32)
        self.assertListEqual(result_arr, array.convert_to_arr())

    def test_delete(self):
        result_arr1 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13]
        array = Da.create_da(15)

        array.delete(0)
        array.delete(13)
        array.delete(5)

        self.assertListEqual(result_arr1, array.convert_to_arr())
        self.assertEqual(array.count, len(result_arr1))

        result_arr2 = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        array = Da.create_da(32)
        for i in range(17):
            array.delete(0)

        self.assertEqual(result_arr2, array.convert_to_arr())
        self.assertEqual(array.capacity, 21)


if __name__ == '__main__':
    unittest.main()
