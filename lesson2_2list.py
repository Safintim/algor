class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, n):
        self.next = n

    def set_prev(self, n):
        self.prev = n


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, v):
        node = self.head

        while node is not None:
            if node.get_value() == v:
                return node
            node = node.get_next()
        return None

    def is_empty(self):
        return self.head is None

    def node_is_tail(self, node):
        return node == self.tail

    def delete(self, v):
        node = self.find(v)

        if node is None:
            return None

        if self.head.get_next() is None:
            self.clean()
        elif self.head == node:
            self.head = self.head.get_next()
            self.head.set_prev(None)
        elif self.node_is_tail(node):
            self.tail = node.get_prev()
            self.tail.set_next(None)
        else:
            node.get_prev().set_next(node.get_next())
            node.get_next().set_prev(node.get_prev())

        return None

    def clean(self):
        self.head = None
        self.tail = None

        return None

    def len(self):
        node = self.head
        length = 0

        while node is not None:
            length += 1
            node = node.get_next()
        return length

    def insert(self, prev, current):
        node_start = self.head

        if self.head is None:
            self.add_in_tail(current)
            return True
        elif self.node_is_tail(prev):
            self.tail = current
            self.tail.set_next(None)
            self.tail.set_prev(prev)
            prev.set_next(current)
            return True

        while node_start is not None:
            if node_start == prev:
                current.set_next(node_start.get_next())
                current.set_prev(node_start)
                node_start.get_next().set_prev(current)
                node_start.set_next(current)
                return True

            node_start = node_start.get_next()

        return False

    def add_in_head(self, item):
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            self.head.set_prev(item)
            item.set_next(self.head)
            self.head = item
            self.head.set_prev(None)

    def convert_list_to_array(self):
        arr = []
        node = self.head

        while node is not None:
            arr.append(node)
            node = node.get_next()

        return arr


def create_list(*args):
    s_list = LinkedList2()
    for i in range(len(args)):
        s_list.add_in_tail(Node(args[i]))

    return s_list



s_list = create_list(1, 3, 2, 3, 4, 5, 3, 6)

# проверка скорости функции del_node
# arr = []
# s = create_list([i for i in range(100000)])
# for i in range(10000):
#     start_time = time.time()
#     s.del_node(10000)
#     arr.append(time.time()-start_time)
#
# result = sum(arr)/len(arr)
# print(result)
