import unittest
import lesson5_stack as l


class StackTest(unittest.TestCase):

    def test_postfix(self):
        result = 59
        self.assertEqual(result, l.postfix('8 2 + 5 * 9 + ='))

    def test_balance_brackets(self):
        stack = l.Stack()
        self.assertTrue(l.balance_brackets('(()((())()))'))
        self.assertTrue(l.balance_brackets('((()))'))
        self.assertFalse(l.balance_brackets('(()()(()'))
        self.assertFalse(l.balance_brackets(')'))

if __name__ == '__main__':
    unittest.main()
