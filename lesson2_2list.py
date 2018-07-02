# print('Двунаправленный Связанный список')
# import time


class Node2:
    def __init__(self, v):
        self.__value = v
        self.__next = None
        self.__prev = None

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_next(self, n):
        self.__next = n

    def set_prev(self, n):
        self.__prev = n


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        """
        Добавляет новый узел в конец списка
        """
        if self.head is None:
            self.head = item
            item.set_next(None)
            item.set_prev(None)
        else:
            self.tail.set_next(item)
            item.set_prev(self.tail)
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
        Находит узел по заданному значению. Поиск идет с головы
        """
        node = self.head

        while node is not None:
            if node.get_value() == v:
                return node
            node = node.get_next()
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

    def clear_list(self):
        """
        1.3 Удаляет все узлы списка
        """
        self.head = None
        self.tail = None

        return None

    def del_node(self, v):
        """
        2.1 Удаляет узел по заданному значению
        """

        if self.head.get_value() == v:
            self.head = self.head.get_next()
            self.head.set_prev(None)
        elif self.tail.get_value() == v:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            if node is not None:
                node.get_prev().set_next(node.get_next())
                node.get_next().set_prev(node.get_prev())
            else:
                return None
        return None

    def del_nodes(self, v):
        """
        1.2 Удаляет все узлы по заданному конкретному значению
        """

        node = self.head
        while node is not None:
            if self.head.get_value() == v:
                self.head = self.head.get_next()
                self.head.set_prev(None)
            elif self.tail.get_value() == v:
                self.tail = self.tail.get_prev()
                self.tail.set_next(None)
            elif node.get_value() == v:
                node.get_prev().set_next(node.get_next())
                node.get_next().set_prev(node.get_prev())
            node = node.get_next()

        return None

    def insert(self, prev, current):
        """
        2.2 Вставка узла после заданного узла
        """
        node_start = self.head

        while node_start is not None:
            if node_start == prev:
                current.set_next(node_start.get_next())
                current.set_prev(node_start)
                node_start.set_next(current)
                node_start.get_next().set_prev(current)

            node_start = node_start.get_next()

        return None

    def add_in_head(self, item):
        """
        Добавляет новый узел в начало списка
        """
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
        s_list.add_in_tail(Node2(args[i]))

    return s_list


s_list = create_list(1, 3, 2, 3, 4, 5, 3, 6)

# s_list.print_all_nodes()
s_list.del_nodes(1)
s_list.print_all_nodes()
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
