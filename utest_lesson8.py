import unittest
import lesson8_order_list as l


class OrderListTest(unittest.TestCase):

    def test_add_node_True(self):
        ord_list = l.create_list(True, 7, 5, 8, -1)
        result = [-1, 5, 7, 8]
        self.assertListEqual(result, list(i.get_value() for i in ord_list.convert_list_to_array()))

    def test_add_node_False(self):
        ord_list = l.create_list(False, 7, 5, 8, -1, -1, -1)
        result = [8, 7, 5, -1, -1, -1]
        self.assertListEqual(result, list(i.get_value() for i in ord_list.convert_list_to_array()))

    def test_find(self):
        ord_list = l.create_list(False, 7, 5, 8, -1, -1, -1)
        self.assertEqual(ord_list.find(100), None)
        self.assertEqual(ord_list.find(-1).get_value(), -1)

    def test_del_node(self):
        ord_list = l.create_list(False, 7, 5, 8, -1, -1, -1)
        result = [8, 7, 5, -1]
        ord_list.del_node(-1)
        ord_list.del_node(-1)
        self.assertListEqual(result, list(i.get_value() for i in ord_list.convert_list_to_array()))


class OrderListStrTest(unittest.TestCase):
    def test_add_node_True(self):
        ord_list = l.create_list(True, 'd', 'c', 'e', 'a')
        result = ['a', 'c', 'd', 'e']
        self.assertListEqual(result, list(i.get_value() for i in ord_list.convert_list_to_array()))

    def test_add_node_False(self):
        ord_list = l.create_list(False, 'd', 'c', 'e', 'a')
        result = ['e', 'd', 'c', 'a']
        self.assertListEqual(result, list(i.get_value() for i in ord_list.convert_list_to_array()))

    def test_find(self):
        ord_list = l.create_list(False, 'd', 'c', 'e', 'a')
        self.assertEqual(ord_list.find('g'), None)
        self.assertEqual(ord_list.find('a').get_value(), 'a')

    def test_del_node(self):
        ord_list = l.create_list(False, 'd', 'c', 'e', 'a', 'a', 'a')
        result = ['e', 'd', 'c', 'a']
        ord_list.del_node('a')
        ord_list.del_node('a')
        self.assertListEqual(result, list(i.get_value() for i in ord_list.convert_list_to_array()))


if __name__ == '__main__':
    unittest.main()
