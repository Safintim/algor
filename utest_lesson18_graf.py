import unittest
import lesson18_graf as l


class GraphTest(unittest.TestCase):

    def test_add_vertex(self):
        g = l.SimpleGraph(4)
        vertexes = [i for i in range(4)]
        for v in vertexes:
            g.AddVertex(v)
        self.assertEqual(len(g.m_adjacency), 4)
        self.assertEqual(len(g.m_adjacency[0]), 4)
        new_vertex = l.Vertex(4)
        g.AddVertex(new_vertex)
        self.assertEqual(len(g.m_adjacency), 5)
        self.assertEqual(len(g.m_adjacency[0]), 5)
        self.assertEqual(g.m_adjacency[0], [0, 0, 0, 0, 0])

    def test_add_edge(self):
        g = l.SimpleGraph(5)
        vertexes = [i for i in range(5)]

        for i in vertexes:
            g.AddVertex(i)

        g.AddEdge(0, 1)
        self.assertListEqual(g.m_adjacency[0], [0, 1, 0, 0, 0])
        self.assertListEqual(g.m_adjacency[1], [1, 0, 0, 0, 0])
        g.AddEdge(4, 1)
        self.assertListEqual(g.m_adjacency[1], [1, 0, 0, 0, 1])
        self.assertListEqual(g.m_adjacency[4], [0, 1, 0, 0, 0])

    def test_remove_vertex(self):
        g = l.SimpleGraph(5)
        vertexes = [i for i in range(5)]

        for v in vertexes:
            g.AddVertex(v)

        g.AddEdge(vertexes[0], vertexes[1])
        g.AddEdge(vertexes[4], vertexes[1])
        g.RemoveVertex(1)

        self.assertListEqual(g.m_adjacency[0], [0, 0, 0, 0])
        self.assertListEqual(g.m_adjacency[1], [0, 0, 0, 0])
        self.assertListEqual(g.m_adjacency[2], [0, 0, 0, 0])
        self.assertListEqual(g.m_adjacency[3], [0, 0, 0, 0])

    def test_remove_edge(self):
        g = l.SimpleGraph(5)
        vertexes = [l.Vertex(i) for i in range(5)]

        for i in vertexes:
            g.AddVertex(i)

        g.m_adjacency = [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
        ]
        g.RemoveEdge(0, 1)
        self.assertListEqual(g.m_adjacency[0], [0, 0, 1, 1, 0])
        self.assertListEqual(g.m_adjacency[1], [0, 0, 0, 1, 1])

    def test_is_edge(self):
        g = l.SimpleGraph(5)
        vertexes = [i for i in range(5)]

        for i in vertexes:
            g.AddVertex(i)

        g.m_adjacency = [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
        ]
        self.assertTrue(g.IsEdge(0, 1))
        self.assertFalse(g.IsEdge(0, 4))
        self.assertTrue(g.IsEdge(3, 2))
        self.assertFalse(g.IsEdge(2, 1))
        new_vert = 10
        self.assertFalse(g.IsEdge(2, new_vert))

    def test_dfs(self):
        g = l.SimpleGraph(5)

        g.AddVertex('A')
        g.AddVertex('B')
        g.AddVertex('C')
        g.AddVertex('D')
        g.AddVertex('E')

        g.m_adjacency = [
            [0, 1, 1, 1, 0],  # A
            [1, 0, 0, 1, 1],  # B
            [1, 0, 0, 1, 0],  # C
            [1, 1, 1, 1, 1],  # D
            [0, 1, 0, 1, 0],  # E
        ]

        self.assertEqual([i.Value for i in g.DepthFirstSearch(0, 1)], ['A', 'B'])
        self.assertEqual([i.Value for i in g.DepthFirstSearch(3, 3)], ['D', 'D'])
        self.assertEqual([i.Value for i in g.DepthFirstSearch(2, 4)], ['C', 'A', 'B', 'E'])
        # self.assertEqual(g.DepthFirstSearch(2, 4), [])

    def test_bfs(self):

        g = l.SimpleGraph(5)

        g.AddVertex('A')
        g.AddVertex('B')
        g.AddVertex('C')
        g.AddVertex('D')
        g.AddVertex('E')

        g.m_adjacency = [
            [0, 1, 1, 1, 0],  # A
            [1, 0, 0, 1, 1],  # B
            [1, 0, 0, 1, 0],  # C
            [1, 1, 1, 1, 1],  # D
            [0, 1, 0, 1, 0],  # E
        ]

        self.assertEqual([i.Value for i in g.BreadthFirstSearch(2, 4)], ['C', 'D', 'E'])
        self.assertEqual([i.Value for i in g.BreadthFirstSearch(4, 2)], ['E', 'D', 'C'])
        self.assertEqual([i.Value for i in g.BreadthFirstSearch(3, 3)], ['D'])
        self.assertEqual([i.Value for i in g.BreadthFirstSearch(1, 2)], ['B', 'A', 'C'])


if __name__ == '__main__':
    unittest.main()
