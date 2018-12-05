import unittest
import lesson1_list as l


class ListTest(unittest.TestCase):

    def test_delete(self):
        s_list = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)
        s_list1 = l.create_list(1)
        arr_list1 = s_list.convert_list_to_array()

        s_list.delete(3)
        s_list1.delete(1)
        arr_list2 = s_list.convert_list_to_array()

        self.assertNotEqual(arr_list1, arr_list2)
        # 1 идет первым значением в списке
        self.assertNotEqual(arr_list1[1], arr_list2[1])
        self.assertEqual(arr_list2[2].get_value(), 3)

    def test_delete2(self):
        s_list = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)
        s_list1 = l.create_list(1, 2, 2, 2)
        arr_list1 = s_list.convert_list_to_array()

        s_list.delete(3, all=True)
        s_list1.delete(2, all=True)

        arr_list2 = s_list.convert_list_to_array()

        self.assertNotEqual(arr_list1, arr_list2)
        self.assertNotEqual(arr_list1[1], arr_list2[1])
        self.assertNotEqual(arr_list1[3], arr_list2[3])
        with self.assertRaises(IndexError):
            print(arr_list2[6])

    def test_clean(self):
        s_list = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)
        arr_list1 = s_list.convert_list_to_array()
        s_list.clean()
        arr_list2 = s_list.convert_list_to_array()

        self.assertNotEqual(arr_list1, arr_list2)
        self.assertEqual(len(arr_list2), 0)

    def test_find_all(self):
        s_list = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)
        arr_list1 = []
        temp = s_list.convert_list_to_array()
        arr_list1.append(temp[1])
        arr_list1.append(temp[3])
        arr_list1.append(temp[6])

        arr_list2 = s_list.find_all(3)
        self.assertEqual(arr_list1, arr_list2)

    def test_len(self):
        s_list = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)

        self.assertEqual(s_list.len(), 8)

    def test_insert(self):
        s_list1 = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)
        s_list2 = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)
        s_list3 = l.create_list()

        arr_list1 = s_list1.convert_list_to_array()

        node1 = l.Node(100)
        node2 = l.Node(10)
        node3 = l.Node(1000)
        result1 = s_list1.insert(arr_list1[len(arr_list1) - 1], node3)
        result2 = s_list2.insert(7, node1)
        result3 = s_list3.insert(None, node2)

        arr_list1 = s_list1.convert_list_to_array()
        arr_list3 = s_list3.convert_list_to_array()
        self.assertTrue(result3)
        self.assertEqual(1, s_list3.len())
        self.assertEqual(10, arr_list3[0].get_value())
        self.assertFalse(result2)
        self.assertTrue(result1)
        self.assertEqual(node3, s_list1.tail)
        self.assertEqual(1000, arr_list1[len(arr_list1) - 1].get_value())

    def test_sum_lists(self):
        s_list1 = l.create_list(1, 2, 3, 4, 5, 6, 7, 8)
        s_list2 = l.create_list(10, 20, 30, 40, 50, 60, 70, 80)

        self.assertTrue(l.sum_lists(s_list1, s_list2))

        sum_lists1 = [11, 22, 33, 44, 55, 66, 77, 88]
        sum_lists2 = l.sum_lists(s_list1, s_list2)

        self.assertListEqual(sum_lists1, sum_lists2)

    def test_iter(self):
        s_list1 = l.create_list(1, 2, 3, 4, 5, 6, 7, 8)
        result = [1, 2, 3, 4, 5, 6, 7, 8]

        self.assertListEqual(result, list((i.get_value() for i in s_list1)))


if __name__ == '__main__':
    unittest.main()