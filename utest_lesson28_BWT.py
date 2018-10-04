import unittest
import lesson28_BWT as l


class MyTestCase(unittest.TestCase):
    def test_generate_random_colors(self):
        bwt = l.BWT()
        for i in range(101):
            colors = set(bwt.generate_random_colors())
            if len(colors) < 2:
                print(colors)
                break
        self.assertEqual(i, 100)

    def test_create_trees(self):
        bwt = l.BWT()
        top = bwt.create_tree(bwt.top_tree)
        print(top.tree)
        # print(bottom.tree)
        self.assertEqual(len(top.tree), 7)


if __name__ == '__main__':
    unittest.main()
