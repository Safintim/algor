class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def first(self):
        self.current = self.head

    def __next__(self):
        if self.current is None:
            self.first()
            raise StopIteration
        temp = self.current
        self.current = self.current.get_next()
        return temp

    def __iter__(self):
        return self

    def node_is_tail(self, node):
        return node == self.tail

    def is_empty(self):
        return self.head is None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            self.current = self.head
        else:
            self.tail.set_next(item)
        self.tail = item

    def print_all_nodes(self):
        node = self.head

        while node is not None:
            print(node.get_value())
            node = node.get_next()

    def find(self, val):
        node = self.head

        while node is not None:
            if node.get_value() == val:
                return node
            node = node.get_next()
        return None

    def find_all(self, val):
        node = self.head
        result_list = []

        while node is not None:
            if node.get_value() == val:
                result_list.append(node)
            node = node.get_next()

        return result_list

    def delete(self, v, all=False):
        node = self.head
        prev = node

        while node is not None:
            if self.head.get_value() == v:
                self.head = self.head.get_next()
                if self.is_empty():
                    self.tail = self.head
                if not all:
                    break
            elif node.get_value() == v:
                prev.set_next(node.get_next())

                if self.node_is_tail(node):
                    self.tail = prev

                if not all:
                    break
                node = prev

            prev = node
            node = node.get_next()

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

    def insert(self, afterNode, newNode):
        node = self.head

        while node is not None:
            if node == afterNode:
                newNode.set_next(node.get_next())
                node.set_next(newNode)
                if self.node_is_tail(node):
                    self.tail = newNode
                return True
            node = node.get_next()
        if afterNode is None and self.head is None:
            self.add_in_tail(newNode)
            return True
        return False

    def convert_list_to_array(self):
        arr = []
        node = self.head

        while node is not None:
            arr.append(node)
            node = node.get_next()

        return arr


def create_list(*args):
    s_list = LinkedList()
    for i in range(len(args)):
        s_list.add_in_tail(Node(args[i]))

    return s_list


def sum_lists(l1, l2):
    if l1.len() != l2.len():
        return False

    result_list = []
    l1_node = l1.head
    l2_node = l2.head

    while l1_node is not None:
        result_list.append(l1_node.get_value() + l2_node.get_value())
        l1_node = l1_node.get_next()
        l2_node = l2_node.get_next()
    return result_list


# arr = []
# s = create_list([i for i in range(1000000)])
# for i in range(10000):
#     start_time = time.time()
#     s.del_node(100000)
#     arr.append(time.time()-start_time)
#
# result = sum(arr)/len(arr)
# print(result)
