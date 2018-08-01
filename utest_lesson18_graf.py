import unittest
import lesson18_graf as l


class GraphTest(unittest.TestCase):

    def test_add_vertex(self):
        g = l.SimpleGraph(4)
        for i in (l.Vertex() for i in range(5)):
            g.add_vertex(i)
        self.assertEqual(len(g.m_adjacency), 5)
        self.assertEqual(len(g.m_adjacency[0]), 5)

    def test_add_edge(self):
        g = l.SimpleGraph(5)
        test_list = [l.Vertex() for i in range(5)]

        for i in test_list:
            g.add_vertex(i)

        g.add_edge(test_list[0], test_list[1])
        g.add_edge(test_list[4], test_list[1])
        self.assertListEqual(g.m_adjacency[0], [0, 1, 0, 0, 0])
        self.assertListEqual(g.m_adjacency[1], [1, 0, 0, 0, 1])
        self.assertListEqual(g.m_adjacency[4], [0, 1, 0, 0, 0])

    def test_remove_edge(self):
        g = l.SimpleGraph(5)
        test_list = [l.Vertex() for i in range(5)]

        for i in test_list:
            g.add_vertex(i)

        g.add_edge(test_list[0], test_list[1])
        g.add_edge(test_list[4], test_list[1])
        g.remove_edge(test_list[1], test_list[4])
        self.assertListEqual(g.m_adjacency[1], [1, 0, 0, 0, 0])
        self.assertListEqual(g.m_adjacency[4], [0, 0, 0, 0, 0])

    def test_remove_vertex(self):
        g = l.SimpleGraph(5)
        test_list = [l.Vertex() for i in range(5)]

        for i in test_list:
            g.add_vertex(i)

        g.add_edge(test_list[0], test_list[1])
        g.add_edge(test_list[4], test_list[1])
        g.remove_vertex(test_list[4])
        self.assertTrue(test_list[4] not in g.vertex)
        self.assertEqual(len(g.vertex), 4)
        self.assertEqual(g.max_vertex, 4)
        self.assertEqual(len(g.m_adjacency), 4)
        self.assertEqual(len(g.m_adjacency[0]), 4)


if __name__ == '__main__':
    unittest.main()
