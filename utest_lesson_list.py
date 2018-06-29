import unittest
import lesson1_list as l


class ListTest(unittest.TestCase):

    def test_del_node(self):
        s_list = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)
        arr_list1 = s_list.convert_list_to_array()

        s_list.del_node(1)

        arr_list2 = s_list.convert_list_to_array()

        self.assertNotEqual(arr_list1, arr_list2)
        # 1 идет первым значением в списке
        self.assertNotEqual(arr_list1[0], arr_list2[0])

    def test_del_nodes(self):
        s_list = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)
        arr_list1 = s_list.convert_list_to_array()

        s_list.del_nodes(3)

        arr_list2 = s_list.convert_list_to_array()

        self.assertNotEqual(arr_list1, arr_list2)
        self.assertNotEqual(arr_list1[1], arr_list2[1])
        self.assertNotEqual(arr_list1[3], arr_list2[3])
        with self.assertRaises(IndexError):
            print(arr_list2[6])

    def test_clear_list(self):
        s_list = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)
        arr_list1 = s_list.convert_list_to_array()
        s_list.clear_list()
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
        s_list = l.create_list(1, 3, 2, 3, 4, 5, 3, 6).convert_list_to_array()

        self.assertEqual(len(s_list), 8)

    def test_insert(self):
        s_list = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)
        node = l.Node(100)

        arr_list1 = s_list.convert_list_to_array()

        s_list.insert(arr_list1[len(arr_list1) - 2], node)

        arr_list1.append(arr_list1[len(arr_list1) - 1])
        arr_list1[len(arr_list1) - 2] = node

        arr_list2 = s_list.convert_list_to_array()

        self.assertEqual(len(arr_list2), 9)
        self.assertListEqual(arr_list1, arr_list2)

    def test_sum_lists(self):
        s_list1 = l.create_list(1, 2, 3, 4, 5, 6, 7, 8)
        s_list2 = l.create_list(10, 20, 30, 40, 50, 60, 70, 80)

        self.assertEqual(len(s_list1), len(s_list2))

        sum_lists1 = [11, 22, 33, 44, 55, 66, 77, 88]
        sum_lists2 = l.sum_lists(s_list1, s_list2)

        self.assertListEqual(sum_lists1, sum_lists2)


if __name__ == '__main__':
    unittest.main()