import unittest
import lesson2_2list as l


class List2Test(unittest.TestCase):

    def test_delete(self):
        s_list = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)
        s_list2 = l.create_list(1)

        s_list2.delete(1)
        self.assertTrue(s_list2.tail is None)
        self.assertTrue(s_list2.head is None)

        arr_list1 = s_list.convert_list_to_array()
        s_list.delete(6)
        arr_list2 = s_list.convert_list_to_array()
        # self.assertNotEqual(arr_list1, arr_list2)
        # если удалить двойку
        # self.assertNotEqual(arr_list1[2], arr_list2[2])
        # self.assertEqual(arr_list2[2].get_value(), 3)
        # если удалить 4
        # self.assertNotEqual(arr_list1[4], arr_list2[4])
        # self.assertEqual(arr_list2[4].get_value(), 5)
        # если удалить голову
        # self.assertNotEqual(arr_list1[0], arr_list2[0])
        # self.assertEqual(arr_list2[0].get_value(), 3)
        # если удалить хвост
        self.assertEqual(len(arr_list2), 7)
        self.assertEqual(arr_list2[6].get_next(), None)
        self.assertEqual(s_list.tail.get_value(), 3)

    def test_insert(self):
        s_list = l.create_list()
        node = l.Node(100)
        r1 = s_list.convert_list_to_array()
        # tail = r1[-1]
        s_list.insert(None, node)
        # print(s_list.tail.get_value())
        self.assertEqual(s_list.tail, node)

    def test_add_in_head(self):

        node1 = l.Node(100)
        node2 = l.Node(200)
        r1 = [node1, node2]

        s_list = l.LinkedList2()
        s_list.add_in_head(node2)
        s_list.add_in_head(node1)

        r2 = s_list.convert_list_to_array()

        self.assertEqual(r1, r2)


if __name__ == '__main__':
    unittest.main()
