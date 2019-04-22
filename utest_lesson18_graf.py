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

        g.AddEdge(vertexes[0], vertexes[1])
        self.assertListEqual(g.m_adjacency[0], [0, 1, 0, 0, 0])
        self.assertListEqual(g.m_adjacency[1], [1, 0, 0, 0, 0])
        g.AddEdge(vertexes[4], vertexes[1])
        self.assertListEqual(g.m_adjacency[1], [1, 0, 0, 0, 1])
        self.assertListEqual(g.m_adjacency[4], [0, 1, 0, 0, 0])

    def test_remove_vertex(self):
        g = l.SimpleGraph(5)
        vertexes = [i for i in range(5)]

        for v in vertexes:
            g.AddVertex(v)

        g.AddEdge(vertexes[0], vertexes[1])
        g.AddEdge(vertexes[4], vertexes[1])
        g.RemoveVertex(vertexes[1])

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
        g.RemoveEdge(vertexes[0], vertexes[1])
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
        self.assertTrue(g.IsEdge(vertexes[0], vertexes[1]))
        self.assertFalse(g.IsEdge(vertexes[0], vertexes[4]))
        self.assertTrue(g.IsEdge(vertexes[3], vertexes[2]))
        self.assertFalse(g.IsEdge(vertexes[2], vertexes[1]))
        new_vert = 10
        self.assertFalse(g.IsEdge(vertexes[2], new_vert))


    def test_dfs(self):

        A = l.Vertex('A')
        B = l.Vertex('B')
        C = l.Vertex('C')
        D = l.Vertex('D')
        E = l.Vertex('E')

        g = l.SimpleGraph(5)

        g.add_vertex(A)
        g.add_vertex(B)
        g.add_vertex(C)
        g.add_vertex(D)
        g.add_vertex(E)

        g.m_adjacency = [
            [0, 1, 1, 1, 0],  # A
            [1, 0, 0, 1, 1],  # B
            [1, 0, 0, 1, 0],  # C
            [1, 1, 1, 1, 1],  # D
            [0, 1, 0, 1, 0],  # E
        ]
        self.assertEqual(g.dfs(A, B), 'A->B')
        self.assertEqual(g.dfs(D, D), 'D->D')
        self.assertEqual(g.dfs(C, E), 'C->A->B->E')
        # self.assertEqual(g.dfs(C, E), None)  # для этой проверки нужно занулить все ребра от Е и к E

    def test_bfs(self):

        A = l.Vertex('A')
        B = l.Vertex('B')
        C = l.Vertex('C')
        D = l.Vertex('D')
        E = l.Vertex('E')

        g = l.SimpleGraph(5)

        g.add_vertex(A)
        g.add_vertex(B)
        g.add_vertex(C)
        g.add_vertex(D)
        g.add_vertex(E)

        g.m_adjacency = [
            [0, 1, 1, 1, 0],  # A
            [1, 0, 0, 1, 1],  # B
            [1, 0, 0, 1, 0],  # C
            [1, 1, 1, 1, 1],  # D
            [0, 1, 0, 1, 0],  # E
        ]
        self.assertEqual(g.bfs(C, E), 'CDE')
        self.assertEqual(g.bfs(E, C), 'EDC')
        self.assertEqual(g.bfs(D, D), 'D')
        self.assertEqual(g.bfs(B, C), 'BAC')


if __name__ == '__main__':
    unittest.main()
