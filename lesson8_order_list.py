class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None

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


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1.get_value() > v2.get_value():
            return 1
        elif v1.get_value() < v2.get_value():
            return -1

        return 0

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

    def add(self, item):

        node = self.head
        if self.head is None:
            self.head = item
            self.tail = item
        else:

            if self.compare(self.head, item) in (0, 1) and self.__ascending:
                self.__add_head(item)
            elif self.compare(item, self.tail) in (0, 1) and self.__ascending:
                self.__add_tail(item)
            elif self.compare(item, self.head) in (0, 1) and self.__ascending is False:
                self.__add_head(item)
            elif self.compare(self.tail, item) in (0, 1) and self.__ascending is False:
                self.__add_tail(item)
            else:
                while node.get_next() is not None:
                    if self.compare(item, node) in (0, 1) and self.compare(node.get_next(), item) in (0, 1) \
                            and self.__ascending:
                        self.__add_inwards(node, item)
                        break
                    elif self.compare(node, item) in (0, 1) and self.compare(item, node.get_next()) in (0, 1) \
                            and self.__ascending is False:
                        self.__add_inwards(node, item)
                        break
                    node = node.get_next()

        return None

    def find(self, v):

        node = self.head
        while node is not None:
            if node.get_value() == v:
                return node

            if self.__ascending:
                if node.get_value() > v:
                    break
            else:
                if node.get_value() < v:
                    break
            node = node.get_next()

        return None

    def delete(self, v):

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

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def get_all(self):
        arr = []
        node = self.head

        while node is not None:
            arr.append(node)
            node = node.get_next()

        return arr

    def len(self):
        return len(self.get_all())

    def print_all_nodes(self):
        """
        Печатает все элементы списка
        """
        node = self.head

        while node is not None:
            print(node.get_value())
            node = node.get_next()


class OrderedListStr(OrderedList):

    def compare(self, v1, v2):
        if v1.get_value().strip() > v2.get_value().strip():
            return 1
        elif v1.get_value().strip() < v2.get_value().strip():
            return -1

        return 0


def create_list(*args):
    s_list = OrderedList(args[0])
    for i in range(1, len(args)):
        s_list.add(Node(args[i]))

    return s_list
