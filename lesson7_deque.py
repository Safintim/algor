"""
ДЕК
"""


class Deque:

    def __init__(self):
        self.queue = []

    def addFront(self, item):
        self.queue.append(item)

    def addTail(self, item):
        self.queue.insert(0, item)

    def removeFront(self):
        if self.size() > 0:
            return self.queue.pop()
        return None

    def removeTail(self):
        if self.size() > 0:
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)


def palindrom(string):

    d = Deque()

    for ch in string:
        d.addFront(ch)

    while d.size() > 1:

        if d.removeFront() != d.removeTail():
            print('Не является полиндромом', end=' ')
            return False

    return True
