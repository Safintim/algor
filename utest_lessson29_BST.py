import unittest
import lesson29_BST as l
import lesson16_bintreeA as l2
import time
from random import randint, shuffle


class MyTestCase(unittest.TestCase):

    def test_halve_arr(self):
        test_list = [12, 7, 4, 14, 5, 11, 5]
        test_list.sort()  # [4, 5, 5, 7, 11, 12, 14]
        result = [
            [4, 5, 5, 7, 11, 12, 14],
            [4, 5, 5], [11, 12, 14],
            [4], [5], [11], [14]
        ]
        bst = l.BST(h=2)

        self.assertEqual(bst.halve_arr(test_list), result)

    def test_add(self):
        test_list = [12, 7, 4, 14, 5, 11, 5]
        result = [7, 5, 12, 4, 5, 11, 14]
        bst = l.BST(h=2)
        bst.add(test_list)

        self.assertEqual(bst.tree, result)

    @staticmethod
    def generate_numbers(h):
        numbers = set()
        while len(numbers) != pow(2, h+1) - 1:
            numbers.add(randint(1, 2 ** (h + 2)))

        numbers = list(numbers)
        shuffle(numbers)
        return numbers

    def test_speed(self):
        h = 16
        test_list = self.generate_numbers(16)
        bin_a = l2.Tree2(len(test_list))
        start_bin_a = time.time()
        for i in test_list:
            bin_a.add(i)
        end_bin_a = time.time() - start_bin_a

        bst = l.BST(h=h)
        start_bst = time.time()
        bst.add(test_list)
        end_bst = time.time() - start_bst

        print('BIN_A:', end_bin_a, sep=' ')
        print('BST:', end_bst, sep=' ')

        self.assertTrue(end_bin_a > end_bst)

    def test_check_keys(self):
        h = 16
        test_list = self.generate_numbers(h)
        tree = l.arr_to_bst(h, test_list)
        for index, value in enumerate(tree):
            if index * 2 + 1 >= len(tree):
                return
            if tree[index * 2 + 1]['key'] < value['key'] \
                    <= tree[index * 2 + 2]['key']:
                pass
            else:
                print(tree[index * 2 + 1]['key'], value['key'],
                      tree[index * 2 + 2]['key'])
                print('Тревога!!')

    def test_check_balance(self):
        h = 16
        test_list = self.generate_numbers(h)

        tree = l.arr_to_bst(h, test_list)
        last_level = -(2 ** h - 1)
        last_nodes = tree[last_level:]

        left_subtree = last_nodes[:len(last_nodes) // 2]
        right_subtree = last_nodes[len(last_nodes) // 2:]

        if not any(left_subtree):
            for node in left_subtree:
                node_i = tree.index(node)
                parent_i = (node_i - 1) // 2
                if tree[parent_i] is not None:
                    self.assertTrue(True)
        elif not any(right_subtree):
            for node in right_subtree:
                node_i = tree.index(node)
                parent_i = (node_i - 1) // 2
                if tree[parent_i] is not None:
                    self.assertTrue(True)
        else:
            return


if __name__ == '__main__':
    unittest.main()
