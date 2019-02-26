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
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:

            if self.compare(self.head, new_node) in (0, 1) and self.__ascending:
                self.__add_head(new_node)
            elif self.compare(new_node, self.tail) in (0, 1) and self.__ascending:
                self.__add_tail(new_node)
            elif self.compare(new_node, self.head) in (0, 1) and self.__ascending is False:
                self.__add_head(new_node)
            elif self.compare(self.tail, new_node) in (0, 1) and self.__ascending is False:
                self.__add_tail(new_node)
            else:
                while node.get_next() is not None:
                    if self.compare(new_node, node) in (0, 1) and self.compare(node.get_next(), new_node) in (0, 1) \
                            and self.__ascending:
                        self.__add_inwards(node, new_node)
                        break
                    elif self.compare(node, new_node) in (0, 1) and self.compare(new_node, node.get_next()) in (0, 1) \
                            and self.__ascending is False:
                        self.__add_inwards(node, new_node)
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

        if node is None:
            return None

        if self.head.get_next() is None:
            self.clean(self.__ascending)
        elif self.head == node:
            self.head = self.head.get_next()
            self.head.set_prev(None)
        elif self.tail == node:
            self.tail = node.get_prev()
            self.tail.set_next(None)
        else:
            node.get_prev().set_next(node.get_next())
            node.get_next().set_prev(node.get_prev())

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
        s_list.add(args[i])

    return s_list
