"""
Стек
"""


class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(0)

    def push(self, value):
        return self.stack.insert(0, value)

    def peak(self):
        if len(self.stack) == 0:
            return None
        return self.stack[0]

    def size(self):
        return len(self.stack)


def postfix(exp):
    stack1 = Stack()
    stack2 = Stack()
    exp = exp.split()[::-1]
    operands = '1234567890'

    for i in exp:
        stack1.push(i)

    while stack1.size() > 0:
        if stack1.peak() in operands:
            stack2.push(stack1.pop())
        else:
            oper = stack1.pop()
            if oper == '+':
                t = int(stack2.pop()) + int(stack2.pop())
                stack2.push(t)
            elif oper == '*':
                t = int(stack2.pop()) * int(stack2.pop())
                stack2.push(t)
            elif oper == '-':
                t = int(stack2.pop()) - int(stack2.pop())
                stack2.push(t)
            elif oper == '/':
                t = int(stack2.pop()) / int(stack2.pop())
                stack2.push(t)
            else:
                return stack2.peak()
    return stack2


def balance_brackets(string):
    stack = Stack()
    open_br = '('
    # close_br = ')'
    flag = True

    for br in string:
        if flag:
            if br == open_br:
                stack.push(br)
            else:
                if stack.size() == 0:
                    flag = False
                else:
                    stack.pop()

    if flag and stack.size() == 0:
        return True
    else:
        return False
