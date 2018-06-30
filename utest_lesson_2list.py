import unittest
import lesson2_2list as l


class List2Test(unittest.TestCase):

    def test_del_node(self):
        s_list = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)
        arr_list1 = s_list.convert_list_to_array()

        s_list.del_node(1)

        arr_list2 = s_list.convert_list_to_array()

        self.assertNotEqual(arr_list1, arr_list2)
        # 1 идет первым значением в списке
        self.assertNotEqual(arr_list1[0], arr_list2[0])

    def test_insert(self):
        s_list = l.create_list(1, 3, 2, 3, 4, 5, 3, 6)
        node = l.Node2(100)
        r1 = s_list.convert_list_to_array()

        s_list.insert(r1[len(r1) - 2], node)

        r1.append(r1[len(r1) - 1])
        r1[len(r1) - 2] = node

        r2 = s_list.convert_list_to_array()

        self.assertEqual(len(r2), 9)
        self.assertListEqual(r1, r2)

    def test_add_in_head(self):

        node1 = l.Node2(100)
        node2 = l.Node2(200)
        r1 = [node1, node2]

        s_list = l.LinkedList2()
        s_list.add_in_head(node2)
        s_list.add_in_head(node1)

        r2 = s_list.convert_list_to_array()

        self.assertEqual(r1, r2)


if __name__ == '__main__':
    unittest.main()