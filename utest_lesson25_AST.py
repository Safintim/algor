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

    def test_parse_exp(self):
        test_str1 = '3 + 5 - 5 + 3'

        result1 = [('скобка', '('), ('скобка', '('), ('число', '3'),
                   ('операция', '+'), ('скобка', '('), ('число', '5'),
                   ('операция', '-'), ('число', '5'), ('скобка', ')'),
                   ('скобка', ')'), ('операция', '+'), ('число', '3'),
                   ('скобка', ')')]

        self.assertListEqual(result1, list((i.token_type, i.token_value) for i in l.parse_exp(test_str1)))


if __name__ == '__main__':
    unittest.main()
