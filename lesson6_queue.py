# import lesson5_stack as Stack
"""
Очереди
"""

class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.size() > 0:
            return self.stack.pop(0)
        return None

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.size() > 0:
            return self.stack[0]
        return None

    def size(self):
        return len(self.stack)


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        if self.size() > 0:
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)


def add_el(q, l):
    for i in l:
        q.enqueue(i)
    return q


# 6.2
def circle_queue(q, n):
    for i in range(n):
        q.enqueue(q.dequeue())

    return q


# 6.3
class Queue2:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        return self.stack1.push(item)

    def dequeue(self):
        if self.stack2.size() > 0:
            return self.stack2.pop()
        else:
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()

    def size(self):
        if self.stack1.size() != 0:
            return self.stack1.size()
        else:
            return self.stack2.size()
