import unittest
import ete3
import lesson28_BWT as l


class MyTestCase(unittest.TestCase):
    def test_generate_random_colors(self):
        bwt = l.BWT()
        for i in range(101):
            colors = set(bwt.generate_random_colors(exclude=[1]))
            print(colors)
            if len(colors) < 2:
                print(colors)
                break
        self.assertEqual(i, 100)

    def test_create_random_tree(self):
        bwt = l.BWT()
        bwt.top_tree = bwt.coloring_random_tree(bwt.top_tree)
        bwt.bottom_tree = bwt.coloring_random_tree(bwt.bottom_tree)

        self.assertNotEqual(bwt.top_tree.tree, bwt.bottom_tree.tree)

    def test_create_mirror_tree(self):
        bwt = l.BWT()
        temp = bwt.coloring_mirror_tree(bwt.top_tree, bwt.bottom_tree)
        self.assertListEqual(temp[0].tree, temp[1].tree)

    def test_create_trees(self):
        bwt = l.BWT()
        top = bwt.create_tree(bwt.top_tree)
        for i in top.tree:
            print('parent {}, left {}, right {}'.format(i.parent_color, i.left_child_color, i.right_child_color))
        self.assertEqual(len(top.tree), 7)

    def test_bind_trees(self):
        bwt = l.BWT()
        bwt.top_tree = bwt.coloring_random_tree(bwt.top_tree)
        bwt.bottom_tree = bwt.coloring_random_tree(bwt.bottom_tree)
        print('base TOP')
        for i in bwt.top_tree.tree:
            print('parent {}, left {}, right {}'.format(i.parent_color,
                                                        i.left_child_color,
                                                        i.right_child_color,))
        print()
        print('base BOTTOM')
        for i in bwt.bottom_tree.tree:
            print('parent {}, left {}, right {}'.format(i.parent_color,
                                                        i.left_child_color,
                                                        i.right_child_color,))
        print()
        # part_top, part_bottom = bwt.bind_trees(bwt.top_tree, bwt.bottom_tree)
        bwt.bind_trees(bwt.top_tree, bwt.bottom_tree)
        part_top = bwt.relationship_trees[-2 ** (bwt.depth - 1):]
        part_bottom = bwt.relationship_trees[:-2 ** (bwt.depth - 1):]
        print('TOP')
        for i in part_top:
            print('parent {}, left {}, right {}, l_child {}, r_child {}'.format(i.parent_color,
                                                        i.left_child_color,
                                                        i.right_child_color,
                                                        i.left_child,
                                                        i.right_child))
        print()
        print('BOTTOM')
        for i in part_bottom:
            print('parent {}, left {}, right {}, l_child {}, r_child {}'.format(i.parent_color,
                                                        i.left_child_color,
                                                        i.right_child_color,
                                                        i.left_child,
                                                        i.right_child))

        print()

    @staticmethod
    def format_tree(tree):
        s = ''

        for i in range(len(tree)):
            l_c = i * 2 + 1
            r_c = i * 2 + 2
            if len(tree) > i * 2 + 2:
                # print('({},{}){}'.format(
                #         str(tree[l_c].left_child_color) + 'l-r' + str(tree[l_c].right_child_color),
                #         str(tree[r_c].left_child_color) + 'l-r' + str(tree[r_c].right_child_color),
                #         str(tree[i].left_child_color) + 'l-r' + str(tree[i].right_child_color)))
                if str(tree[i]) in s:
                    s = s.replace(str(tree[i]), '({},{}){}'.format(
                        str(tree[r_c].left_child_color) + 'l--r' + str(tree[r_c].right_child_color),
                        str(tree[l_c].left_child_color) + 'l--r' + str(tree[l_c].right_child_color),

                        str(tree[i].left_child_color) + 'l--r' + str(tree[i].right_child_color)))
                    continue
                s = '({},{}){}'.format(
                    tree[i * 2 + 2],
                    tree[i * 2 + 1],
                    str(tree[i].left_child_color) + 'l--r' + str(tree[i].right_child_color))
        return s

    def test_print(self):
        # a = l.BWT.COLORS
        bwt = l.BWT()
        bwt.top_tree = bwt.coloring_random_tree(bwt.top_tree)
        bwt.bottom_tree = bwt.coloring_random_tree(bwt.bottom_tree)
        part_top, part_bottom = bwt.bind_trees(bwt.top_tree, bwt.bottom_tree)

        tree1 = self.format_tree(bwt.top_tree.tree) + ';'
        tree2 = self.format_tree(bwt.bottom_tree.tree) + ';'

        t1 = ete3.Tree(tree1, format=1)
        t2 = ete3.Tree(tree2, format=1)

        print(t1.get_ascii(attributes=["name", ]))
        print()
        print(t2.get_ascii(attributes=["name", ]))


if __name__ == '__main__':
    unittest.main()
