#!/usr/bin/python3
# -*- coding: utf-8 -*-
from lesson14_tree import SimpleTree, TreeNode


# Узел AST
class ANode:
    def __init__(self, token_type, token_value):
        self.token_type = token_type
        self.token_value = token_value


# Парсер выражения
class ParseExpression:

    def __init__(self):
        self.OPERATOR = 300
        self.NUMBER = 200
        self.OPEN_BRACKET = 100
        self.CLOSE_BRACKET = 101

    @staticmethod
    def find_start_end(flag, result, i):
        """
        Находит начало и конец аргументов
        """
        brackets = 1
        if flag:
            j = i + 2
            while brackets != 0:
                if result[j] == '(':
                    brackets += 1
                elif result[j] == ')':
                    brackets -= 1
                j += 1
        else:
            j = i - 2
            while brackets != 0:
                if result[j] == '(':
                    brackets -= 1
                elif result[j] == ')':
                    brackets += 1
                j -= 1

        return j

    def add_brackets(self, operator, s):
        result = s.split()
        i = 0
        while i <= len(result) - 1:
            if result[i] == operator:
                if i + 2 <= len(result) - 1:  # чтобы избежать IndexError

                    if result[i - 1] == ')':  # если перед стоит закр скобка, то нужно найти начало аргумента
                        j = self.find_start_end(False, result, i)
                        result.insert(j + 1, '(')
                        i += 1
                    elif result[i - 2] != '(':  # если нет скобочек, то поставить скобочку
                        result.insert(i - 1, '(')
                        i += 1

                    if result[i+1] == '(':  # если после стоит откр скобка, то нужно найти конец аргумента
                        j = self.find_start_end(True, result, i)
                        result.insert(j, ')')
                        i += 1
                    elif result[i+2] != ')':  # если нет, то поставить
                        result.insert(i+2, ')')
                        i += 1

                else:  # если сюда попали, значит, это конец строки и в конце нет скобки
                    result.insert(i + 2, ')')

                    if result[i - 1] != ')':
                        result.insert(i - 1, '(')
                    if result[i - 1] == ')':
                        j = self.find_start_end(False, result, i)
                        result.insert(j + 1, '(')
                        i += 1

            i += 1
        return ' '. join(result)

    def parse_exp(self, exp):
            operators = ['/', '*', '-', '+']
            brackets = ['(', ')']
            token_list = []

            for op in operators:
                exp = self.add_brackets(op, exp)

            exp = exp.split()

            for elem in exp:
                if elem in operators:
                    token_list.append(ANode(self.OPERATOR, elem))
                elif elem in brackets[0]:
                    token_list.append(ANode(self.OPEN_BRACKET, elem))
                elif elem in brackets[1]:
                    token_list.append(ANode(self.CLOSE_BRACKET, elem))
                elif elem != ' ':
                    token_list.append(ANode(self.NUMBER, elem))

            return token_list


# AST
class AST:
    def __init__(self):
        self.tree = SimpleTree(TreeNode(None, None))
        self.node = self.tree.root

    def create(self, exp):
        parser = ParseExpression()
        token_list = parser.parse_exp(exp)
        index = 0

        while len(token_list) > 0:
            if token_list[0].token_type == parser.OPEN_BRACKET:
                token_list.pop(0)
                self.tree.add_node(self.node, TreeNode(self.node, None))
                self.node = self.node.child[0]
            elif token_list[0].token_type == parser.CLOSE_BRACKET:
                token_list.pop(0)
                self.node = self.node.parent
            elif token_list[0].token_type == parser.NUMBER:
                self.node.value = token_list.pop(0).token_value
                self.node = self.node.parent
            elif token_list[0].token_type == parser.OPERATOR:
                self.node.value = token_list.pop(0).token_value
                self.tree.add_node(self.node, TreeNode(self.node, None))
                self.node = self.node.child[1]
        return self.tree
