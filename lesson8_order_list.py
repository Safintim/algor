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


class OrderedList:
    def __init__(self, inc):
        self.head = None
        self.tail = None
        self.increase = inc

    def print_all_nodes(self):
        """
        Печатает все элементы списка
        """
        node = self.head

        while node is not None:
            print(node.get_value())
            node = node.get_next()

    @staticmethod
    def compare_value(left, right):
        if left.get_value() >= right.get_value():
            return True
        else:
            return False

    def __add_head(self, item):

        self.head.set_prev(item)
        item.set_next(self.head)
        self.head = item
        self.head.set_prev(None)

    def __add_tail(self, item):

        item.set_prev(self.tail)
        item.set_next(None)
        self.tail.set_next(item)
        self.tail = item

    @staticmethod
    def __add_inwards(node, item):
        node.get_next().set_prev(item)
        item.set_next(node.get_next())
        item.set_prev(node)
        node.set_next(item)

    def add_node(self, item):

        node = self.head
        if self.head is None:
            self.head = item
            self.tail = item
        else:

            # Так как в цикле идет проверка текущего и следующего,
            # нужно позаботиться о том, чтобы создать этот следующий
            if self.compare_value(self.head, item) and self.increase:
                self.__add_head(item)
            elif self.compare_value(item, self.tail) and self.increase:
                self.__add_tail(item)
            elif self.compare_value(item, self.head) and self.increase is False:
                self.__add_head(item)
            elif self.compare_value(self.tail, item) and self.increase is False:
                self.__add_tail(item)
            else:
                while node.get_next() is not None:
                    # можно выполнить проверку типа item.value > node.item
                    # Если по возрастанию
                    if self.compare_value(item, node) and self.compare_value(node.get_next(), item)\
                            and self.increase:
                        self.__add_inwards(node, item)
                        break
                    # Если по убыванию
                    elif self.compare_value(node, item) and self.compare_value(item, node.get_next())\
                            and self.increase is False:
                        self.__add_inwards(node, item)
                        break
                    node = node.get_next()
        return None

    def find(self, v):

        node = self.head
        while node is not None:
            if node.get_value() > v and self.increase:
                print('Такого нет')
                return None
            elif node.get_value() == v:
                return node
            elif node.get_value() < v and self.increase is False:
                print('Такого нет')
                return None
            node = node.get_next()

        return None

    def del_node(self, v):

        node = self.find(v)
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

    def convert_list_to_array(self):
        arr = []
        node = self.head

        while node is not None:
            arr.append(node)
            node = node.get_next()

        return arr


class OrderedListStr(OrderedList):

    @staticmethod
    def compare_value(left, right):
        if left.get_value().strip() >= right.get_value().strip():
            return True
        else:
            return False


def create_list(*args):
    s_list = OrderedList(args[0])
    for i in range(1, len(args)):
        s_list.add_node(Node2(args[i]))

    return s_list
