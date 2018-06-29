# print('Связной список')

class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        """
        Добавляет новый узел в конец списка
        """
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        """
        Печатает все элементы списка
        """
        node = self.head

        while node is not None:
            print(node.value)
            node = node.next

    def find(self, v):
        """
        Находит узел по заданному значению
        """
        node = self.head

        while node is not None:
            if node.value == v:
                return node
            node = node.next
        return None

    def del_node(self, v):
        """
        1.1 Удаляет узел по заданному значению
        """
        node = self.head
        prev = node

        while node is not None:
            if self.head.value == v:
                self.head = self.head.next
                break

            elif node.value == v:
                prev.next = node.next

                # кажется эти строчки не обязательны. питон сам очистит память
                node.value = None
                node.next = None
                break

            prev = node
            node = node.next

        return None

    def del_nodes(self, v):
        """
        1.2 Удаляет все узлы по заданному конкретному значению
        """
        node = self.head
        prev = node

        while node is not None:
            if self.head.value == v:
                self.head = self.head.next

            elif node.value == v:
                prev.next = node.next
                node = prev
            prev = node
            node = node.next

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
            if node.value == v:
                result_list.append(node)
            node = node.next

        return result_list

    def __len__(self):
        """
        1.5 Возвращает число узлов списка
        """
        node = self.head
        length = 0

        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, prev, current):
        """
        1.6 Вставка узла после заданного узла
        """
        node = self.head

        while node is not None:
            if node == prev:
                current.next = node.next
                node.next = current
            node = node.next

        return None

    def convert_list_to_array(self):
        arr = []
        node = self.head

        while node is not None:
            arr.append(node)
            node = node.next

        return arr


def sum_lists(l1, l2):
    if len(l1) != len(l2):
        return 'Не равны размеры'

    result_list = []
    l1_node = l1.head
    l2_node = l2.head

    while l1_node is not None:
        result_list.append(l1_node.value + l2_node.value)
        l1_node = l1_node.next
        l2_node = l2_node.next
    return result_list


def create_list(*args):
    s_list = LinkedList()
    for i in range(len(args)):
        s_list.add_in_tail(Node(args[i]))

    return s_list

