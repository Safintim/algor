"""
ДЕК
"""


class Deque:

    def __init__(self):
        self.queue = []

    def add_front(self, item):
        self.queue.append(item)

    def add_tail(self, item):
        self.queue.insert(0, item)

    def remove_front(self):
        if self.size() > 0:
            return self.queue.pop()
        return None

    def remove_tail(self):
        if self.size() > 0:
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)


def palindrom(string):

    d = Deque()

    for ch in string:
        d.add_front(ch)

    while d.size() > 1:

        if d.remove_front() != d.remove_tail():
            print('Не является полиндромом', end=' ')
            return False

    return True
