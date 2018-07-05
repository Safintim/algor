import lesson5_stack as Stack
"""
Очереди
"""


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
test_list = ['Python', 'C++', 'C#', 'Java', 'Ruby', 'R', 'JavaScript', 'PHP',
             'Django', 'Rails', 'Laravel', 'PyQT5', 'GIT', 'SQL', 'HTML5/CSS3']


def add_el(q, l):
    for i in l:
        q.enqueue(i)
    return q


# 6.2
def circle_queue(q, n):
    for i in range(n):
        q.enqueue(q.dequeue())

    return q


q = add_el(q, test_list)
# print(q.items)
# circle_queue(q, 1)
# print(q.items)


# 6.3
class Queue2:
    def __init__(self):
        self.stack1 = Stack.Stack()
        self.stack2 = Stack.Stack()

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



q2 = Queue2()
q2 = add_el(q2, test_list)
print(q2.stack1.stack, 'stack1')
print(q2.stack2.stack, 'stack2')

# r = ['HTML5/CSS3', 'SQL', 'GIT', 'PyQT5', 'Laravel', 'Rails', 'Django', 'PHP', 'JavaScript', 'R']
# q2.dequeue()
# q2.dequeue()
# q2.dequeue()
# q2.dequeue()
# q2.dequeue()
# circle_queue(q2, 1)
# print('ПОсле ')
# print(q2.stack1.stack, 'stack1')
# print(q2.stack2.stack, 'stack2')

# circle_queue(q, 1)
# print(q.items)