#!/usr/bin/python3
# -*- coding: utf-8 -*-
from lesson14_tree import SimpleTree, TreeNode


# Узел AST
class ANode:
    def __init__(self, token_type, token_value):
        self.token_type = token_type
        self.token_value = token_value
        self.translate = self.token_value


# Парсер выражения
class ParseExpression:

    def __init__(self):
        self.OPERATOR = 300
        self.NUMBER = 200
        self.OPEN_BRACKET = 100
        self.CLOSE_BRACKET = 101

    @staticmethod
    def find_start_arg(tokens, i):
        """
        Находит начало
        """
        brackets = 1
        j = i - 2
        while brackets != 0:
            if tokens[j] == '(':
                brackets -= 1
            elif tokens[j] == ')':
                brackets += 1
            j -= 1
        return j

    @staticmethod
    def find_end_arg(tokens, i):
        """
        Находит конец
        """
        brackets = 1
        j = i + 2
        while brackets != 0:
            if tokens[j] == '(':
                brackets += 1
            elif tokens[j] == ')':
                brackets -= 1
            j += 1
        return j

    def add_brackets_for_operator(self, operator, math_expression):
        tokens = math_expression.split()
        i = 0
        open_bracket = '('
        close_bracket = ')'

        while i <= len(tokens) - 1:
            if tokens[i] == operator:
                if i + 2 <= len(tokens) - 1:  # чтобы избежать IndexError
                    # Если перед стоит закр скобка,
                    # то нужно найти начало аргумента.
                    if tokens[i - 1] == close_bracket:
                        start_arg = self.find_start_arg(tokens, i)
                        tokens.insert(start_arg + 1, open_bracket)
                        i += 1
                    # Если нет скобочек, то поставить скобочку.
                    elif tokens[i - 2] != open_bracket:
                        tokens.insert(i - 1, open_bracket)
                        i += 1
                    # Если после стоит откр скобка,
                    # то нужно найти конец аргумента.
                    if tokens[i + 1] == open_bracket:
                        end_arg = self.find_end_arg(tokens, i)
                        tokens.insert(end_arg, close_bracket)
                        i += 1
                    # Если нет, то поставить ).
                    elif tokens[i + 2] != close_bracket:
                        tokens.insert(i + 2, close_bracket)
                        i += 1
                # Если сюда попали, значит, это конец строки
                # и в конце нет скобки.
                else:
                    tokens.insert(i + 2, close_bracket)

                    if tokens[i - 1] != close_bracket:
                        tokens.insert(i - 1, open_bracket)
                    if tokens[i - 1] == close_bracket:
                        start_arg = self.find_start_arg(tokens, i)
                        tokens.insert(start_arg + 1, open_bracket)
                        i += 1

            i += 1
        return ' '. join(tokens)

    def add_brackets(self, operators, math_expression):
        for operator in operators:
            math_expression = self.add_brackets_for_operator(
                operator, math_expression)

        return math_expression

    def parse_exp(self, math_expression):
            operators = ['/', '*', '-', '+']
            open_bracket = '('
            close_bracket = ')'
            whitespace = ' '
            token_list = []

            math_expression = self.add_brackets(operators, math_expression)

            for token in math_expression.split():
                if token in operators:
                    token_list.append(ANode(self.OPERATOR, token))
                elif token == open_bracket:
                    token_list.append(ANode(self.OPEN_BRACKET, token))
                elif token == close_bracket:
                    token_list.append(ANode(self.CLOSE_BRACKET, token))
                elif token != whitespace:
                    token_list.append(ANode(self.NUMBER, token))

            return token_list


# AST
class AST:
    def __init__(self):
        self.tree = SimpleTree(TreeNode(None, None))
        self.current_node = self.tree.root

    def create(self, math_expression):
        parser = ParseExpression()
        token_list = parser.parse_exp(math_expression)
        left = 0
        right = 1

        while len(token_list) > 0:
            if token_list[0].token_type == parser.OPEN_BRACKET:
                token_list.pop(0)
                self.tree.add_node(self.current_node, TreeNode(self.current_node, None))
                self.current_node = self.current_node.child[left]
            elif token_list[0].token_type == parser.CLOSE_BRACKET:
                token_list.pop(0)
                self.current_node = self.current_node.parent
            elif token_list[0].token_type == parser.NUMBER:
                self.current_node.value = token_list.pop(0)
                self.current_node = self.current_node.parent
            elif token_list[0].token_type == parser.OPERATOR:
                self.current_node.value = token_list.pop(0)
                self.tree.add_node(self.current_node, TreeNode(self.current_node, None))
                self.current_node = self.current_node.child[right]
        return self.tree


class Interpreter:
    def __init__(self, tree):
        self.tree = tree
        self.current_node = self.tree.root

    def execution(self, node):
        if (self.current_node == self.tree.root and self.current_node.value.token_type == 200):
            return (
                self.current_node.value.token_value,
                self.current_node.value.translate,
                self.current_node.value.token_value
                == eval(self.current_node.value.translate))
        elif self.current_node and self.current_node.child:
            l_c = self.current_node.child[0]
            r_c = self.current_node.child[1]
            if (l_c.value.token_type == ParseExpression().NUMBER and
                    r_c.value.token_type == ParseExpression().NUMBER):
                if '/' == self.current_node.value.token_value:
                    self.current_node.value.token_value = (int(l_c.value.token_value)
                                                           // int(r_c.value.token_value))
                elif '*' == self.current_node.value.token_value:
                    self.current_node.value.token_value = (int(l_c.value.token_value)
                                                           * int(r_c.value.token_value))
                elif '-' == self.current_node.value.token_value:
                    self.current_node.value.token_value = (int(l_c.value.token_value)
                                                           - int(r_c.value.token_value))
                else:
                    self.current_node.value.token_value = (int(l_c.value.token_value)
                                                           + int(r_c.value.token_value))

                if self.current_node.value.translate == '/':
                    self.current_node.value.translate = '({}{}/{})'.format(
                        l_c.value.translate,
                        self.current_node.value.translate,
                        r_c.value.translate
                    )
                else:
                    self.current_node.value.translate = '({}{}{})'.format(
                        l_c.value.translate,
                        self.current_node.value.translate,
                        r_c.value.translate
                    )
                self.current_node.value.token_type = ParseExpression().NUMBER
                self.current_node.child.pop()
                self.current_node.child.pop()

                if self.current_node.parent:
                    self.current_node = self.current_node.parent

                return self.execution(self.current_node)

            elif (l_c.value.token_type == ParseExpression().OPERATOR or
                  r_c.value.token_type == ParseExpression().OPERATOR):
                if l_c.value.token_type == ParseExpression().OPERATOR:
                    self.current_node = l_c
                else:
                    self.current_node = r_c

                return self.execution(self.current_node)
