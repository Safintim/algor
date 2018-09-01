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
        parse_exp = l.ParseExpression()
        for op in test_operators:
            test_str1 = parse_exp.add_brackets(op, test_str1)
        for op in test_operators:
            test_str2 = parse_exp.add_brackets(op, test_str2)
        for op in test_operators:
            test_str3 = parse_exp.add_brackets(op, test_str3)
        self.assertEqual(test_str1, result1)
        self.assertEqual(test_str2, result2)
        self.assertEqual(test_str3, result3)

    def test_parse_exp(self):
        test_str1 = '3 + 5 - 5 + 3'
        p_e = l.ParseExpression()
        result1 = [(100, '('), (100, '('), (200, '3'),
                   (300, '+'), (100, '('), (200, '5'),
                   (300, '-'), (200, '5'), (101, ')'),
                   (101, ')'), (300, '+'), (200, '3'),
                   (101, ')')]
        self.assertListEqual(result1, list((i.token_type, i.token_value) for i in p_e.parse_exp(test_str1)))

    def test_create(self):
        test_str1 = '3 + 5 - 5 + 3'
        ast1 = l.AST().create(test_str1)
        result1 = ['+', '+', '3', '-', '5', '5', '3']

        test_str2 = '7 + 3 / 25 * ( 5 - 2 )'
        ast2 = l.AST().create(test_str2)
        result2 = ['+', '7', '*', '/', '3', '25', '-', '5', '2']

        self.assertListEqual(result1, [i.value for i in ast1.traverse_tree(ast1.root)])
        self.assertListEqual(result2, [i.value for i in ast2.traverse_tree(ast2.root)])


if __name__ == '__main__':
    unittest.main()
