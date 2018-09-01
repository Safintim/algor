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
        OPERATOR = 300
        NUMBER = 200
        OPEN_BRACKET = 100
        CLOSE_BRACKET = 101
        test_str1 = '3 + 5 - 5 + 3'
        p_e = l.ParseExpression()
        result1 = [(OPEN_BRACKET, '('), (OPEN_BRACKET, '('), (NUMBER, '3'),
                   (OPERATOR, '+'), (OPEN_BRACKET, '('), (NUMBER, '5'),
                   (OPERATOR, '-'), (NUMBER, '5'), (CLOSE_BRACKET, ')'),
                   (CLOSE_BRACKET, ')'), (OPERATOR, '+'), (NUMBER, '3'),
                   (CLOSE_BRACKET, ')')]
        self.assertListEqual(result1, list((i.token_type, i.token_value) for i in p_e.parse_exp(test_str1)))

    def test_create(self):
        test_str1 = '3 + 5 - 5 + 3'
        ast1 = l.AST().create(test_str1)
        result1 = ['+', '+', '3', '-', '5', '5', '3']

        test_str2 = '7 + 3 / 25 * ( 5 - 2 )'
        ast2 = l.AST().create(test_str2)
        result2 = ['+', '7', '*', '/', '3', '25', '-', '5', '2']

        self.assertListEqual(result1, [i.value.token_value for i in ast1.traverse_tree(ast1.root)])
        self.assertListEqual(result2, [i.value.token_value for i in ast2.traverse_tree(ast2.root)])

    def test_execution(self):
        test_str1 = '3 + 5 - 5 + 3'
        ast1 = l.AST().create(test_str1)
        inter1 = l.Interpreter(ast1)
        result1 = (6, '((3+(5-5))+3)')

        test_str2 = '7 + 3 / 25 * ( 5 - 2 )'
        ast2 = l.AST().create(test_str2)
        inter2 = l.Interpreter(ast2)
        result2 = (7, '(7+((3/25)*(5-2)))')
        self.assertEqual(result1, inter1.execution(ast1.root))
        self.assertEqual(result2, inter2.execution(ast2.root))


if __name__ == '__main__':
    unittest.main()
