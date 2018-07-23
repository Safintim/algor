# print('Связной список')
# import time


class Node:
    def __init__(self, v):
        self.__value = v
        self.__next = None

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_next(self, n):
        self.__next = n


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def first(self):
        self.current = self.head

    def __next__(self):
        if self.current is None:
            raise StopIteration
        temp = self.current
        self.current = self.current.get_next()
        return temp

    def __iter__(self):
        self.first()
        return self

    def add_in_tail(self, item):
        """
        Добавляет новый узел в конец списка
        """
        if self.head is None:
            self.head = item
            self.current = self.head
        else:
            self.tail.set_next(item)
        self.tail = item

    def print_all_nodes(self):
        """
        Печатает все элементы списка
        """
        node = self.head

        while node is not None:
            print(node.get_value())
            node = node.get_next()

    def find(self, v):
        """
        Находит узел по заданному значению
        """
        node = self.head

        while node is not None:
            if node.get_value() == v:
                return node
            node = node.get_next()
        return None

    def del_node(self, v):
        """
        1.1 Удаляет узел по заданному значению
        """
        node = self.head
        prev = node

        while node is not None:
            if self.head.get_value() == v:
                self.head = self.head.get_next()
                break

            elif node.get_value() == v:
                prev.set_next(node.get_next())
                break

            prev = node
            node = node.get_next()

        return None

    def del_nodes(self, v):
        """
        1.2 Удаляет все узлы по заданному конкретному значению
        """
        node = self.head
        prev = node

        while node is not None:
            if self.head.get_value() == v:
                self.head = self.head.get_next()

            elif node.get_value() == v:
                prev.set_next(node.get_next())
                node = prev
            prev = node
            node = node.get_next()

        return None

    def clear_list(self):
        """
        1.3 Удаляет все узлы списка
        """
        self.head = None
        self.tail = None

        return None

    def find_all(self, v):
        """
        1.4 Находит все узлы по заданному конкретному значению
        На выходе массив узлов
        """
        node = self.head
        result_list = []

        while node is not None:
            if node.get_value() == v:
                result_list.append(node)
            node = node.get_next()

        return result_list

    def __len__(self):
        """
        1.5 Возвращает число узлов списка
        """
        node = self.head
        length = 0

        while node is not None:
            length += 1
            node = node.get_next()
        return length

    def insert(self, prev, current):
        """
        1.6 Вставка узла после заданного узла
        """
        node = self.head

        while node is not None:
            if node == prev:
                current.set_next(node.get_next())
                node.set_next(current)
                break
            node = node.get_next()

        return None

    def convert_list_to_array(self):
        arr = []
        node = self.head

        while node is not None:
            arr.append(node)
            node = node.get_next()

        return arr


def sum_lists(l1, l2):
    if len(l1) != len(l2):
        return False

    result_list = []
    l1_node = l1.head
    l2_node = l2.head

    while l1_node is not None:
        result_list.append(l1_node.get_value() + l2_node.get_value())
        l1_node = l1_node.get_next()
        l2_node = l2_node.get_next()
    return result_list


def create_list(*args):
    s_list = LinkedList()
    for i in range(len(args)):
        s_list.add_in_tail(Node(args[i]))

    return s_list


# arr = []
# s = create_list([i for i in range(1000000)])
# for i in range(10000):
#     start_time = time.time()
#     s.del_node(100000)
#     arr.append(time.time()-start_time)
#
# result = sum(arr)/len(arr)
# print(result)
s_list1 = create_list(1, 2, 3, 4, 5, 6, 7, 8)
itr = s_list1
while True:
    try:
        a = next(itr)
    except StopIteration:
        break
    print(itr.current)


while True:
    try:
        a = next(itr)
    except StopIteration:
        break
    print(itr.current)

# for i in s_list1:
#     print(i.get_value())
#
# for i in s_list1:
#     print(i.get_value())