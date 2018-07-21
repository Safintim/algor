import unittest
import lesson6_queue as l


class QueueTest(unittest.TestCase):

    def test_circle_queue(self):
        q = l.Queue()
        test_list = ['Python', 'C++', 'C#', 'Java', 'Ruby', 'R', 'JavaScript', 'PHP',
                     'Django', 'Rails', 'Laravel', 'PyQT5', 'GIT', 'SQL', 'HTML5/CSS3']

        result = ['Ruby', 'Java', 'C#', 'C++', 'Python', 'HTML5/CSS3', 'SQL', 'GIT',
                  'PyQT5', 'Laravel', 'Rails', 'Django', 'PHP', 'JavaScript', 'R']
        q = l.add_el(q, test_list)
        l.circle_queue(q, 5)
        self.assertListEqual(result, q.items)

    def test_circle_queue2(self):
        q = l.Queue2()
        test_list = ['Python', 'C++', 'C#', 'Java', 'Ruby', 'R', 'JavaScript', 'PHP',
                     'Django', 'Rails', 'Laravel', 'PyQT5', 'GIT', 'SQL', 'HTML5/CSS3']
        result = ['Ruby', 'Java', 'C#', 'C++', 'Python', 'HTML5/CSS3', 'SQL', 'GIT',
                  'PyQT5', 'Laravel', 'Rails', 'Django', 'PHP', 'JavaScript', 'R']
        q = l.add_el(q, test_list)
        l.circle_queue(q, 5)
        self.assertListEqual(result, q.stack1.stack + q.stack2.stack[::-1])


if __name__ == '__main__':
    unittest.main()
