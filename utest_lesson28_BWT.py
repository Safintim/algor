import unittest
import ete3
import lesson28_BWT as l


class MyTestCase(unittest.TestCase):
    @staticmethod
    def create_bwt():
        bwt = l.BWT()
        bwt.coloring_random_tree(bwt.top_tree)
        bwt.coloring_random_tree(bwt.bottom_tree)
        return bwt

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
        bwt = self.create_bwt()
        # bwt.top_tree = bwt.coloring_random_tree(bwt.top_tree)
        # bwt.bottom_tree = bwt.coloring_random_tree(bwt.bottom_tree)
        print([i.id for i in bwt.top_tree.tree])
        print([i.id for i in bwt.bottom_tree.tree])

        self.assertNotEqual(bwt.top_tree.tree, bwt.bottom_tree.tree)

    def test_copy_colors(self):
        bwt = l.BWT()
        bwt.coloring_random_tree(bwt.top_tree)
        bwt.copy_colors(bwt.top_tree, bwt.bottom_tree)
        r1 = [(i.parent_color, i.left_child_color, i.right_child_color) for i in
              bwt.top_tree.tree]
        r2 = [(i.parent_color, i.left_child_color, i.right_child_color) for i in
              bwt.bottom_tree.tree]
        print([i.id for i in bwt.top_tree.tree])
        print([i.id for i in bwt.bottom_tree.tree])
        self.assertEqual(r1, r2)

    def test_create_mirror_tree(self):
        bwt = l.BWT()
        bwt.coloring_mirror_tree(bwt.top_tree, bwt.bottom_tree)
        r1 = [(i.parent_color, i.left_child_color, i.right_child_color) for i in
              bwt.top_tree.tree]
        r2 = [(i.parent_color, i.left_child_color, i.right_child_color) for i in
              bwt.bottom_tree.tree]
        print([i.id for i in bwt.top_tree.tree])
        print([i.id for i in bwt.bottom_tree.tree])
        self.assertListEqual(r1, r2)

    def test_get_node(self):
        bwt = self.create_bwt()
        bwt.bind_trees(bwt.top_tree, bwt.bottom_tree)
        self.assertEqual(bwt.get_node(id=14), None)
        self.assertEqual(bwt.get_node(id=2).id, 2)

    def test_create_trees(self):
        bwt = l.BWT()
        top = bwt.create_tree(bwt.top_tree)
        for i in top.tree:
            print('parent {}, left {}, right {}'.format(
                i.parent_color,
                i.left_child_color,
                i.right_child_color))
        self.assertEqual(len(top.tree), 7)

    def test_bind_trees(self):
        bwt = self.create_bwt()
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
        bwt.bind_trees(bwt.top_tree, bwt.bottom_tree)
        part_top = bwt.relationship_trees[-2 ** (bwt.depth - 1):]
        part_bottom = bwt.relationship_trees[:-2 ** (bwt.depth - 1):]
        print('TOP')
        for i in part_top:
            print('parent {}, left {}, right {}, l_child {}, r_child {}'.format(
                i.parent_color,
                i.left_child_color,
                i.right_child_color,
                i.left_child,
                i.right_child))
        print()
        print('BOTTOM')
        for i in part_bottom:
            print('parent {}, left {}, right {}, l_child {}, r_child {}'.format(
                i.parent_color,
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
                if str(tree[i]) in s:
                    s = s.replace(str(tree[i]), '({},{}){}'.format(
                        tree[r_c],
                        tree[l_c],
                        tree[i]))
                    continue
                s = '({},{}){}'.format(
                    tree[r_c],
                    tree[l_c],
                    tree[i])

        for i in range(len(tree)):
            if str(tree[i]) in s:
                s = s.replace(str(tree[i]), '{}l--r{}'.format(
                    tree[i].left_child_color,
                    tree[i].right_child_color))
        return s

    @staticmethod
    def format_relation(relation):
        print('relationship_trees')
        for i in range(len(relation)):

            print('Node {}: parent_color {}, left_color {}, right_color {};'
                  ' left_child p-l-r {}, right_child p-l-r {}'.format(
                    i,
                    relation[i].parent_color,
                    relation[i].left_child_color,
                    relation[i].right_child_color,
                    (relation[i].left_child.parent_color,
                     relation[i].left_child.left_child_color,
                     relation[i].left_child.right_child_color),
                    (relation[i].right_child.parent_color,
                     relation[i].right_child.left_child_color,
                     relation[i].right_child.right_child_color),))

    def test_print(self):
        bwt = self.create_bwt()
        # bwt.coloring_mirror_tree(bwt.top_tree, bwt.bottom_tree)
        bwt.bind_trees(bwt.top_tree, bwt.bottom_tree)

        tree1 = self.format_tree(bwt.top_tree.tree) + ';'
        tree2 = self.format_tree(bwt.bottom_tree.tree) + ';'

        t1 = ete3.Tree(tree1, format=1)
        t2 = ete3.Tree(tree2, format=1)

        print('TOP Tree')
        print(t1.get_ascii(attributes=["name", ]))
        print()

        self.format_relation(bwt.relationship_trees)
        print()
        print('BOTTOM Tree')
        print(t2.get_ascii(attributes=["name", ]))

        return bwt

    def test_find_all_paths(self):
        bwt = self.test_print()

        paths_top = bwt.find_all_paths_tree(bwt.top_tree)
        paths_bottom = bwt.find_all_paths_tree(bwt.bottom_tree)
        r1 = []
        r2 = []
        for path in paths_top.values():
            for node in path:
                r1.append(
                    (node.parent_color,
                     node.left_child_color,
                     node.right_child_color))

        for path in paths_bottom.values():
            for node in path:
                r2.append(
                    (node.parent_color,
                     node.left_child_color,
                     node.right_child_color))
        print(r1)
        print(r2)
        return paths_top, paths_bottom, bwt

    def test_counting_colors_all_paths(self):
        paths_top, paths_bottom, bwt = self.test_find_all_paths()
        count_colors_top = bwt.counting_colors_all_paths(paths_top, 1)
        count_colors_bottom = bwt.counting_colors_all_paths(paths_bottom, 1)
        print()
        for node, count in count_colors_top.items():
            print((node.parent_color, count), end=',')
        print()
        for node, count in count_colors_bottom.items():
            print((node.parent_color, count), end=',')

    def test_find_all_paths_bwt(self):
        bwt = self.test_print()
        for path in bwt.find_all_paths_bwt(1):
            print(path)

    def test_optimal_way(self):
        bwt = self.test_print()
        path, color = bwt.optimal_way(color=1, mn=True)
        print(color)
        print([(node.parent_color,
                node.left_child_color,
                node.right_child_color) for node in path])

    def test_random_walk(self):
        bwt = self.create_bwt()
        bwt.bind_trees(bwt.top_tree, bwt.bottom_tree)
        result = []
        for i in range(10000):
            result.append(bwt.random_walk(29)[1])

        print(sum(result) / len(result))

    def test_quantum_walk(self):
        bwt = self.create_bwt()
        bwt.bind_trees(bwt.top_tree, bwt.bottom_tree)
        result = []
        print(bwt.quantum_walk(29))
        # for i in range(10000):
        #     result.append(bwt.random_walk(29)[1])
        #
        # print(sum(result) / len(result))


if __name__ == '__main__':
    unittest.main()
