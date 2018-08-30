import unittest
import lesson25_AST as l


class ASTTest(unittest.TestCase):
    def test_add_brackets(self):
        test_str1 = '7 + 3 / 25 * ( 5 - 2 )'
        test_str2 = '3 + 5 - 5 + 3'
        test_str3 = '7 + 3 * 5 - 2'
        result1 = '( 7 + ( ( 3 / 25 ) * ( 5 - 2 ) ) )'
        result2 = '( ( 3 + ( 5 - 5 ) ) + 3 )'
        result3 = '( 7 + ( ( 3 * 5 ) - 2 ) )'

        test_operators = ['/', '*', '-', '+']
        for op in test_operators:
            test_str1 = l.add_brackets(op, test_str1)
        for op in test_operators:
            test_str2 = l.add_brackets(op, test_str2)
        for op in test_operators:
            test_str3 = l.add_brackets(op, test_str3)
        self.assertEqual(test_str1, result1)
        self.assertEqual(test_str2, result2)
        self.assertEqual(test_str3, result3)


if __name__ == '__main__':
    unittest.main()
