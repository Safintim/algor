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
        node_start = self.head
        node_end = self.tail

        while node_start != node_end:
            if self.head.get_value() == v:
                self.head = self.head.get_next()
                self.head.set_prev(None)
                break
            elif self.tail.get_value() == v:
                self.tail = self.tail.get_prev()
                self.tail.set_next(None)
                break
            else:
                if node_start.get_value() == v:
                    node_start.get_prev().set_next(node_start.get_next())
                    node_start.get_next().set_prev(node_start.get_prev())
                    break
                elif node_end.get_value() == v:
                    node_end.get_next().set_prev(node_end.get_prev())
                    node_end.get_prev().set_next(node_end.get_next())
                    break

            node_start = node_start.get_next()
            node_end = node_end.get_prev()

        return None

    def insert(self, prev, current):
        """
        2.2 Вставка узла после заданного узла
        """
        node_start = self.head
        node_end = self.tail
        while node_start != node_end:
            if node_start == prev:
                current.set_next(node_start.get_next())
                current.set_prev(node_start)
                node_start.set_next(current)
                node_start.get_next().set_prev(current)
            elif node_end == prev:
                current.set_next(node_end.get_next())
                current.set_prev(node_end)
                node_end.set_prev(current)
                node_end.get_prev().set_next(current)
            node_start = node_start.get_next()
            node_end = node_start.get_prev()

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
